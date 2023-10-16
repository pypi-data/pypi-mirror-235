from __future__ import annotations

import abc
import asyncio

from loguru import logger
from sona.core.inferencer import InferencerBase
from sona.core.storage.base import StorageBase
from sona.core.utils.common import import_class
from sona.settings import settings
from sona.worker.consumers import ConsumerBase
from sona.worker.messages import Context, Job, State
from sona.worker.producers import ProducerBase

TOPIC_PREFIX = settings.SONA_WORKER_TOPIC_PREFIX


class WorkerBase:
    name: str = None
    topic: str = "dummy"

    def set_consumer(self, consumer: ConsumerBase):
        self.consumer = consumer

    def set_producer(self, producer: ProducerBase):
        self.producer = producer

    def set_storage(self, storage: StorageBase):
        self.storage = storage

    async def start(self):
        await self.on_load()
        self.topic = self.get_topic()
        logger.info(f"Susbcribe on {self.topic}({self.consumer.__class__.__name__})")
        self.consumer.subscribe(self.topic)
        async for message in self.consumer.consume():
            try:
                context = Context.model_validate_json(message)
                await self.on_context(context)
            except Exception as e:
                logger.warning(f"[{self.topic}] error: {e}, msg: {message}")

    @classmethod
    def get_topic(cls) -> str:
        return f"{TOPIC_PREFIX}{cls.name}" if cls.name else cls.topic

    @classmethod
    def load_class(cls, import_str):
        worker_cls = import_class(import_str)
        if worker_cls not in cls.__subclasses__():
            raise Exception(f"Unknown worker class: {import_str}")
        return worker_cls

    # Callbacks
    @abc.abstractmethod
    async def on_load(self) -> None:
        return NotImplemented

    @abc.abstractmethod
    async def on_context(self, message: Context) -> Context:
        return NotImplemented


class InferencerWorker(WorkerBase):
    def __init__(self, inferencer: InferencerBase):
        super().__init__()
        self.inferencer = inferencer

    async def on_load(self):
        logger.info(f"Loading inferencer: {self.inferencer.name}")
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.inferencer.on_load)

    async def on_context(self, context: Context):
        try:
            logger.info(f"[{self.topic}] recv: {context.to_message()}")
            for topic in context.supervisors:
                self.producer.emit(topic, context.to_message())

            # Prepare process data
            current_job: Job = context.current_job
            current_state: State = State.start(current_job.name)
            params = current_job.prepare_params(context.results)
            files = current_job.prepare_files(context.results)
            files = self.storage.pull_all(context.id, files)

            # Process
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                None, self.inferencer.inference, params, files
            )

            # NOTE: special case for s3 storage
            s3meta = {}
            for file in files:
                s3meta.update(file.metadata.get("s3", {}))
            result = result.mutate(
                files=self.storage.push_all(
                    context.id, result.files, metadata={"s3": s3meta}
                )
            )

            # Create success context
            current_state = current_state.complete()
            next_context = context.next_context(current_state, result)
            logger.info(f"[{self.topic}] success: {next_context.to_message()}")

            # Emit message
            for topic in next_context.supervisors:
                self.producer.emit(topic, next_context.to_message())
            next_job = next_context.current_job
            if next_job:
                self.producer.emit(next_job.topic, next_context.to_message())
            else:
                for topic in next_context.reporters:
                    self.producer.emit(topic, next_context.to_message())
            return next_context

        except Exception as e:
            # Create fail context
            current_state = current_state.fail(e)
            next_context = context.next_context(current_state)
            logger.exception(f"[{self.topic}] error: {next_context.to_message()}")

            # Emit message
            for topic in next_context.fallbacks:
                self.producer.emit(topic, next_context.to_message())
            return next_context

        finally:
            self.storage.clean(context.id)

    def get_topic(self):
        return f"{TOPIC_PREFIX}{self.inferencer.name}"

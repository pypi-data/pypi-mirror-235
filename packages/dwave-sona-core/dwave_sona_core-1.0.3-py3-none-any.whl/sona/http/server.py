import asyncio

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger
from sona.core.inferencer import InferencerBase
from sona.core.messages.result import Result
from sona.core.storage import StorageBase, create_storage
from sona.http.messages import SonaRequest, SonaResponse
from sona.settings import settings

INFERENCER_CLASS = settings.SONA_INFERENCER_CLASS

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@api.on_event("startup")
async def startup():
    api.storage: StorageBase = create_storage()
    api.inferencer: InferencerBase = InferencerBase.load_class(INFERENCER_CLASS)()
    api.inferencer.on_load()


@api.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, err: RequestValidationError):
    logger.warning(f"Client Error: {request}, {err.errors()}")
    resp = SonaResponse(code="400", message=str(err.errors()))
    return JSONResponse(status_code=400, content=resp.model_dump())


@api.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, err: Exception):
    logger.exception(f"Server Error: {request}")
    resp = SonaResponse(code="500", message=str(err))
    return JSONResponse(status_code=500, content=resp.model_dump())


@api.get("/ping")
async def ping():
    return SonaResponse(message="pong")


@api.post("/inference")
async def inference(request: SonaRequest):
    inferencer: InferencerBase = api.inferencer
    storage: StorageBase = api.storage
    try:
        files = storage.pull_all(request.context_id, request.files)
        loop = asyncio.get_running_loop()
        result: Result = await loop.run_in_executor(
            None, inferencer.inference, request.params, files
        )

        # NOTE: special case for s3 storage
        s3meta = {}
        for file in files:
            s3meta.update(file.metadata.get("s3", {}))
        result = result.mutate(
            files=storage.push_all(
                request.context_id, result.files, metadata={"s3": s3meta}
            )
        )
        logger.info(f"[{inferencer.name}] success: {request.model_dump_json()}")
        return SonaResponse(result=result)
    except Exception as e:
        raise e
    finally:
        storage.clean(request.context_id)

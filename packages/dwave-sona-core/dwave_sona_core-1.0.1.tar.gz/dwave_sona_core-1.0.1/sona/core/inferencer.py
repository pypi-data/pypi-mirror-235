from __future__ import annotations

import abc
from typing import Any, Dict, List

import click
from pydantic import BaseModel, Field
from sona.core.messages import File, Result
from sona.core.utils.common import import_class


class DefaultInputFilesSchema(BaseModel):
    default: str = Field(None, description="origin file")


class InferencerBase:
    name: str = NotImplemented
    description: str = ""
    input_params_schema: BaseModel = None
    input_files_schema: BaseModel = DefaultInputFilesSchema()
    result_data_schema: BaseModel = None
    result_files_schema: BaseModel = None

    # Callbacks
    def on_load(self) -> None:
        return

    @abc.abstractmethod
    def inference(self, params: Dict, files: List[File]) -> Result:
        return NotImplemented

    @abc.abstractmethod
    def cancel(self) -> None:
        return

    @classmethod
    def load_class(cls, import_str):
        inferencer_cls = import_class(import_str)
        if inferencer_cls not in cls.__subclasses__():
            raise Exception(f"Unknown inferencer class: {import_str}")
        return inferencer_cls

    def cmd(self, *args: Any, **kwds: Any) -> Any:
        param_props, file_props = {}, {}
        if self.input_params_schema:
            schema = self.input_params_schema.model_json_schema()
            param_props = schema["properties"]
        if self.input_files_schema:
            schema = self.input_files_schema.model_json_schema()
            file_props = schema["properties"]

        def run(**kwargs):
            files = []
            for prop in file_props:
                val = kwargs.pop(prop)
                if val:
                    files.append(File(label=prop, path=val))
            self.on_load()
            result = self.inference(params=kwargs, files=files)
            print(result.model_dump_json())

        func = run
        for name, prop in param_props.items():
            option = click.option(
                f"--{name}",
                default=prop.get("default"),
                help=prop.get("description"),
                metavar=f'<{prop.get("type")}>',
            )
            func = option(func)
        for name, prop in file_props.items():
            option = click.argument(name, metavar=f"<filepath:{name}>")
            func = option(func)
        func.__doc__ = self.description
        click.command()(func)()

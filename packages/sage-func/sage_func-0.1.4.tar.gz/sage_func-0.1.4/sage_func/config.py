from typing import Optional, Type

from pydantic import BaseModel, Field, ValidationError

from sage_func.services.defaultvectordb_service import DefaultVectorDBService
from sage_func.types.abstract_vectordb import AbstractVectorDB
from sage_func.types.log_level import LogLevel
from sage_func.utils.file_utilities import generate_functions_map
from sage_func.utils.format_config_args import format_config_args


class Config(BaseModel):
    openai_key: str
    openai_url: str
    functions_directory: Optional[str] = Field(
        "functions", description="The directory of functions."
    )
    vectordb: Optional[Type[AbstractVectorDB]] = Field(
        DefaultVectorDBService, description="VectorDB class reference."
    )
    log_level: Optional[LogLevel] = Field(
        LogLevel.ERROR, description="The desired log level for output."
    )

    class Config:
        arbitrary_types_allowed = True


_config = Config(openai_key="", openai_url="")
function_map = {}


def set_config(**kwargs):
    """Set the configuration parameters."""
    global _config
    global function_map
    try:
        kwargs = format_config_args(**kwargs)
        _config = Config(**kwargs)
        function_map = generate_functions_map()
        return _config
    except ValidationError as e:
        raise ValidationError(f"Invalid configuration: {e}")


def get_config():
    """Retrieve the configuration."""
    return _config


def get_function_map():
    return function_map

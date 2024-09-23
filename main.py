from contextlib import asynccontextmanager
import logging
from typing import Literal
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from setup_logging import setup_logging
from postcode_validator.postcode_service_builder import PostcodeServiceBuilder
from postcode_validator.enums import PostcodeType
from postcode_loader import load_postcodes_from_file

setup_logging()
postcodes_cache = set()

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifecycle_manager(app: FastAPI):
    """
    Application lifecyle manager.
    Load postcode cache at start up and clean up at shutdown.
    """
    global postcodes_cache
    try:
        postcodes_cache = await load_postcodes_from_file("postcodes.txt")
    except:
        error_message = "Error loading postcodes cache."
        logger.exception(error_message)
        raise RuntimeError(error_message)
    yield
    logger.info("Server gracefully shutdown.")


app = FastAPI(lifespan=lifecycle_manager)


class PostcodeNormalizer(BaseModel):
    postcode: str = Field(
        min_length=6,
        max_length=8,
        description="Postcode that will be validated.",
    )
    postcode_type: Literal[PostcodeType.UK]


@app.post("/api/v1/postcode/validate")
async def validate(request: Request, params: PostcodeNormalizer):
    """
    Validates a postcode using the given parameters.
    Args:
        request (Request): The request object.
        params (PostcodeNormalizer): The post code parameters.
    Returns:
        JSONResponse: The response containing the validation result.
    Raises:
        HTTPException: If there is an error validating the post code.
    """

    logger.debug(f"Validating postcode: {params}")
    postcode_service = PostcodeServiceBuilder.build(
        params.postcode_type, postcodes_cache
    )

    try:
        result = postcode_service.validate(params.postcode)
    except Exception as e:
        error_message = f"Error validating postcode: {e}"
        logger.exception(error_message)
        raise HTTPException(status_code=500, detail=error_message)

    return JSONResponse(
        content={
            "valid": result.get("valid"),
            "postcode": result.get("postcode"),
        }
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)

import logging
from postcode_validator.enums import PostcodeType
from postcode_validator.services.postcode_service_interface import (
    PostcodeServiceInterface,
)
from postcode_validator.services.uk_postcode_service import UKPostcodeService
from postcode_validator.exceptions import InvalidPostcodeException


logger = logging.getLogger(__name__)


class PostcodeServiceBuilder:
    """
    Factory class to build the appropriate PostcodeService based on the postcode type.
    """

    POSTCODE_TYPES = {PostcodeType.UK: UKPostcodeService}

    @classmethod
    def build(cls, postcode_type: str, cache: set = set()) -> PostcodeServiceInterface:
        postcode_service = cls.POSTCODE_TYPES.get(postcode_type)
        if postcode_service is not None:
            logger.info(f"Building {postcode_type} service instance.")
            return postcode_service(cache)
        else:
            error_message = f"Unknown postcode type: {postcode_type}."
            logger.error(error_message)
            raise InvalidPostcodeException(error_message)

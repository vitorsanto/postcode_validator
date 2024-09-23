import logging
from typing import Dict
from postcode_validator.services.postcode_service_interface import (
    PostcodeServiceInterface,
)
from postcode_validator.validators.uk_postcode_validator import UKPostcodeValidator
from postcode_validator.formatters.uk_postcode_formatter import UKPostcodeFormatter

logger = logging.getLogger(__name__)


class UKPostcodeService(PostcodeServiceInterface):
    """
    Class that encapsulates the business logic responsible for validating and formatting UK postcodes.
    Attributes:
        _validators (UKPostcodeValidator): An instance of UKPostcodeValidator used for validation.
        _formatter (UKPostcodeFormatter): An instance of UKPostcodeFormatter used for formatting postcodes.
    Args:
        _cache (set): A set used to store valid postcodes that acts a cache.
    """

    def __init__(self, cache: set = set()):
        self._validator = UKPostcodeValidator()
        self._formatter = UKPostcodeFormatter()
        self._cache = cache

    def validate(self, raw_postcode: str) -> Dict[bool, str]:
        """
        Validates a raw postcode.
        Args:
            raw_postcode (str): The raw postcode to be validated.
        Returns:
            dict: A dictionary containing the validation result and the formatted postcode.
                - valid (bool): True if the postcode is valid, False otherwise.
                - postcode (str): The formatted postcode if valid, raw postcode otherwise.
        """
        formatted_postcode = self._formatter.format(raw_postcode)

        if self._check_cache(formatted_postcode) or self._validator.is_valid(
            formatted_postcode
        ):
            logger.info(f"Postcode {formatted_postcode} is valid.")
            return {"valid": True, "postcode": formatted_postcode}
        else:
            logger.info(f"Postcode {formatted_postcode} is invalid.")
            return {"valid": False, "postcode": raw_postcode}

    def _check_cache(self, formatted_postcode: str):
        """
        Checks if the formatted postcode is present in the cache.
        Args:
            formatted_postcode (str): The formatted postcode to check.
        Returns:
            True if the postcode is present in the cache, False otherwise.
        """
        if formatted_postcode in self._cache:
            logger.info(f"Postcode {formatted_postcode} found in cache.")
            return True
        return False

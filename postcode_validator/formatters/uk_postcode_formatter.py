import re
from postcode_validator.formatters.postcode_formatter_interface import (
    PostcodeFormatterInterface,
)


class UKPostcodeFormatter(PostcodeFormatterInterface):
    """
    Class responsible for formatting UK postcodes.
    Attributes:
        UK_POSTCODE_FORMATTER_REGEX (re.Pattern): A regular expression pattern used to strip unwanted characters from the postcodes.
    """

    UK_POSTCODE_FORMATTER_REGEX = re.compile(r"[^a-zA-Z0-9]")

    def format(self, postcode: str) -> str:
        """
        Formats the given UK postcode.
        Args:
            postcode (str): The UK postcode to be formatted.
        Returns:
            formatted postcode (str): The formatted UK postcode.
        """
        formatted_postcode: str = self.UK_POSTCODE_FORMATTER_REGEX.sub("", postcode)
        formatted_postcode = f"{formatted_postcode[:-3]} {formatted_postcode[-3:]}"
        return formatted_postcode.upper()

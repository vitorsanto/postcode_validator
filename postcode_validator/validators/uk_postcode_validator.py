import re
from .postcode_validator_interface import PostcodeValidatorInterface


class UKPostcodeValidator(PostcodeValidatorInterface):
    """
    Class responsible for validating UK postcodes.
    Attributes:
        UK_POSTCODE_REGEX (re.Pattern): A regular expression pattern used to validate UK postcodes.
        Ref: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    """

    UK_POSTCODE_REGEX = re.compile(
        r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$",
        re.IGNORECASE,
    )

    def is_valid(self, postcode: str) -> bool:
        """
        Validates if the given postcode is a valid UK postcode.
        Args:
            postcode (str): The postcode to be validated.
        Returns:
            bool: True if the postcode is valid, False otherwise.
        """
        return self.UK_POSTCODE_REGEX.match(postcode)

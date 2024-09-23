class InvalidPostcodeException(Exception):
    """
    Custom exception for invalid postcode.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message: str = "Invalid postcode"):
        self.message: str = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

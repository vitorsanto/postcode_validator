from abc import ABC, abstractmethod


class PostcodeValidatorInterface(ABC):
    """
    Interface for postcode validators.
    """

    @abstractmethod
    def is_valid(cls, postcode: str) -> bool:
        pass

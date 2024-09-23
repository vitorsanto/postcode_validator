from abc import ABC, abstractmethod


class PostcodeFormatterInterface(ABC):
    """
    Interface for formatting postcodes.
    """

    @abstractmethod
    def format(cls, postcode: str) -> bool:
        pass

from abc import ABC, abstractmethod
from typing import Dict


class PostcodeServiceInterface(ABC):
    """
    Interface for a postcode service that provides postcode validation.
    """

    @abstractmethod
    def validate(self, postcode: str) -> Dict[bool, str]:
        pass

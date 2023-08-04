from abc import ABCMeta, abstractmethod
from typing import List

from ...domain.room import Room


class RepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def list(self) -> List[Room]:
        pass


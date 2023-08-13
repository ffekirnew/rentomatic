from abc import ABCMeta, abstractmethod
from typing import List

from bson import ObjectId


class RepositoyInterface(metaclass=ABCMeta):
    @abstractmethod
    def list(self) -> List:
        pass

    @abstractmethod
    def add(self, room: object) -> None:
        pass

    @abstractmethod
    def get(self, id: ObjectId) -> object:
        pass

    @abstractmethod
    def update(self, id: ObjectId, room: object) -> None:
        pass

    @abstractmethod
    def delete(self, id: ObjectId) -> None:
        pass

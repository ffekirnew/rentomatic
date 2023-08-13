from abc import abstractmethod
from typing import List

from bson import ObjectId

from use_cases.dtos.room.room_dto import RoomDto
from use_cases.services.interfaces.repository_interface import \
    RepositoyInterface


class RoomRepositoryInterface(RepositoyInterface):
    @abstractmethod
    def list(self) -> List[RoomDto]:
        pass

    @abstractmethod
    def add(self, room: RoomDto) -> None:
        pass

    @abstractmethod
    def get(self, id: ObjectId) -> RoomDto:
        pass

    @abstractmethod
    def update(self, id: ObjectId, room: RoomDto) -> None:
        pass

    @abstractmethod
    def delete(self, id: ObjectId) -> None:
        pass

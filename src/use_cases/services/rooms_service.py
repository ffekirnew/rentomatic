from typing import List

from bson import ObjectId

from domain.entities.room import Room
from use_cases.dtos.room.create_room_dto import CreateRoomDto
from use_cases.services.interfaces.room_repository_interface import \
    RoomRepositoryInterface


class RoomsService:
    def __init__(self, repository: RoomRepositoryInterface) -> None:
        self.repository = repository

    def get_all(self) -> List[Room]:
        return self.repository.list()

    def add(self, room: CreateRoomDto) -> None:
        return self.repository.add(room)

    def get(self, id: ObjectId) -> Room:
        return self.repository.get(id)

    def update(self, id: ObjectId, room: Room) -> None:
        return self.repository.update(id, room)

    def delete(self, id: ObjectId) -> None:
        return self.repository.delete(id)

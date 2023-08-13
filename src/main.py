from typing import List

from bson import ObjectId

from domain.entities.room import Room
from infrastructure.persistence.memory_repository import MemoryRepository
from use_cases.dtos.room.create_room_dto import CreateRoomDto
from use_cases.services.rooms_service import RoomsService

if __name__ == "__main__":
    rooms: List[Room] = [
        CreateRoomDto(5, 15.0, 15.5, 15.5),
        CreateRoomDto(5, 15.0, 15.5, 15.5),
    ]

    repo = MemoryRepository([])
    rooms_service = RoomsService(repo)

    print(rooms_service.get_all())
    print(rooms_service.get(ObjectId("64d8b4f63da64a3bab4a66f5")))

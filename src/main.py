from typing import List
from uuid import uuid4
from infrastructure.memory_repository import MemoryRepository
from domain.room import Room
from use_cases.rooms_use_case import RoomsUseCase


if __name__ == "__main__":
    rooms: List[Room] = [
        Room(uuid4(), 5, 15.0, 15.5, 15.5),
        Room(uuid4(), 5, 15.0, 15.5, 15.5),
    ]
    repo = MemoryRepository([])
    rooms_service = RoomsUseCase(repo)

    print(rooms_service.GetAll())
    rooms_service.Add(rooms[0])
    print(rooms_service.GetAll())
    rooms_service.Add(rooms[1])
    print(rooms_service.GetAll())

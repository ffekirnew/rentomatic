from typing import Dict, List
from typing_extensions import override
from domain.room import Room
from use_cases.interfaces.repository_interface import RepositoryInterface


class MemoryRepository(RepositoryInterface):
    def __init__(self, data: List[Dict[str, object]]) -> None:
        self.rooms = data

    @override
    def list(self) -> List[Room]:
        return [Room.from_dict(room) for room in self.rooms]

    @override
    def add(self, room: Room) -> None:
        self.rooms.append(room.to_dict())

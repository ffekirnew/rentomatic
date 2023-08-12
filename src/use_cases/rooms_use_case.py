from domain.room import Room
from use_cases.interfaces.repository_interface import RepositoryInterface


class RoomsUseCase:
    def __init__(self, repository: RepositoryInterface) -> None:
        self.repository = repository

    def GetAll(self):
        return self.repository.list()

    def Add(self, room: Room) -> None:
        return self.repository.add(room)

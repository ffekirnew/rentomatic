from abc import ABCMeta, abstractmethod
from typing import List

from bson import ObjectId

from use_cases.dtos.user.create_user_dto import CreateUserDto
from use_cases.dtos.user.user_dto import UserDto


class UserServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def list(self) -> List[UserDto]:
        pass

    @abstractmethod
    def add(self, user: CreateUserDto) -> None:
        pass

    @abstractmethod
    def verify_password(self, user: CreateUserDto, password: str) -> bool:
        pass

    @abstractmethod
    def get(self, id: ObjectId) -> UserDto:
        pass

    @abstractmethod
    def get_user_by_user_name(self, username: str) -> UserDto:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> UserDto:
        pass

    @abstractmethod
    def update(self, id: ObjectId, user: CreateUserDto) -> None:
        pass

    @abstractmethod
    def delete(self, id: ObjectId) -> None:
        pass

from typing import List

import bcrypt
from bson import ObjectId

from use_cases.dtos.user.create_user_dto import CreateUserDto
from use_cases.dtos.user.user_dto import UserDto
from use_cases.services.interfaces.user_repository_interface import \
    UserRepositoyInterface
from use_cases.services.interfaces.user_service_interface import \
    UserServiceInterface


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoyInterface) -> None:
        self.user_repository = user_repository

    def list(self) -> List[UserDto]:
        self.user_repository.list()

    def add(self, user: CreateUserDto) -> None:
        user.salt = bcrypt.gensalt()
        user.password = bcrypt.hashpw(user.password.encode("utf-8"), user.salt)
        self.user_repository.add(user)

    def verify_password(self, user: CreateUserDto, password: str) -> bool:
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), user.salt)
        return hashed_password == user.password

    def get(self, id: ObjectId) -> UserDto:
        self.user_repository.get(id)

    def get_user_by_user_name(self, username: str) -> UserDto:
        self.user_repository.get_user_by_user_name(username)

    def get_user_by_email(self, email: str) -> UserDto:
        self.user_repository.get_user_by_email(email)

    def update(self, id: ObjectId, user: CreateUserDto) -> None:
        self.user_repository.update(id, user)

    def delete(self, id: ObjectId) -> None:
        self.user_repository.delete(id)

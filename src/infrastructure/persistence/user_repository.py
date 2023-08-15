from typing import Dict, List

from bson import ObjectId
from pymongo import MongoClient

from use_cases.dtos.user.create_user_dto import CreateUserDto
from use_cases.dtos.user.user_dto import UserDto
from use_cases.services.interfaces.user_repository_interface import \
    UserRepositoyInterface

conn_string = ""


class UserRepository(UserRepositoyInterface):
    def __init__(self, data: List[Dict[str, object]]):
        self.data = data
        self.client = MongoClient(conn_string)
        self.db = self.client.rentomatic
        self.users = self.db.users

    def list(self) -> List[UserDto]:
        return [UserDto.from_dict(user) for user in list(self.user.find())]

    def add(self, user: CreateUserDto) -> ObjectId:
        user_id = self.users.insert_one(user).inserted_id
        return user_id

    def get(self, id: ObjectId) -> UserDto:
        return UserDto.from_dict(self.users.find_one({"_id": id}))

    def update(self, id: ObjectId, room: CreateUserDto) -> None:
        return self.users.update_one({"_id": id}, {"$set": room})

    def delete(self, id: ObjectId) -> None:
        return self.users.delete_one({"_id": id})

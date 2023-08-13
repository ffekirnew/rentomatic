from typing import Dict, List

from bson import ObjectId
from pymongo import MongoClient

from use_cases.dtos.room.room_dto import RoomDto
from use_cases.dtos.room.create_room_dto import CreateRoomDto
from use_cases.services.interfaces.room_repository_interface import \
    RoomRepositoryInterface

conn_string = "mongodb+srv://ffekirnew:KA8VG3Id6rU242xE@cluster0.ybkwa1w.mongodb.net/expense_tracker"


class MemoryRepository(RoomRepositoryInterface):
    def __init__(self, data: List[Dict[str, object]]) -> None:
        self.data = data
        self.client = MongoClient(conn_string)
        self.db = self.client.rentomatic
        self.rooms = self.db.rooms

    def initialize(self):
        self.rooms.insert_many(self.data)

    def list(self) -> List[RoomDto]:
        return [RoomDto.from_dict(room) for room in list(self.rooms.find())]

    def get(self, id: ObjectId) -> RoomDto:
        return RoomDto.from_dict(self.rooms.find_one({"_id": id}))

    def add(self, room: CreateRoomDto) -> ObjectId:
        return self.rooms.insert_one(room.to_dict()).inserted_id

    def delete(self, id: ObjectId) -> None:
        return self.rooms.delete_one({"_id": id})

    def update(self, id: ObjectId, room: RoomDto) -> None:
        return self.rooms.update_one({"_id": id}, {"$set": room})

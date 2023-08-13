import dataclasses

from bson import ObjectId


@dataclasses.dataclass
class User:
    _id: ObjectId
    nickname: str
    username: str
    email: str
    salt: str
    password: str

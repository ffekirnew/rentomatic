import dataclasses

from bson import ObjectId


@dataclasses.dataclass
class UserDto:
    _id: ObjectId
    nickname: str
    username: str
    email: str
    salt: str
    password: str

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

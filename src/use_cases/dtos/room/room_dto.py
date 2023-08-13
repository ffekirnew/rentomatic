import dataclasses

from bson import ObjectId


@dataclasses.dataclass()
class RoomDto:
    _id: ObjectId
    size: int
    price: float
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

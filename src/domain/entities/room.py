import dataclasses

from bson import ObjectId


@dataclasses.dataclass()
class Room:
    _id: ObjectId
    size: int
    price: float
    longitude: float
    latitude: float

import dataclasses


@dataclasses.dataclass
class CreateRoomDto:
    size: int
    price: float
    longitude: float
    latitiude: float

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

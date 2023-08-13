import dataclasses


@dataclasses.dataclass
class CreateUserDto:
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

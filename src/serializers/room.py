import json
from ..domain.room import Room


class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o: Room) -> dict:
        try:
            return {
                "code": o.code,
                "size": o.size,
                "price": o.price,
                "longitude": o.longitude,
                "latitude": o.latitude
            }
        except AttributeError:
            return super().default(o)

from .infrastructure.memory_repository import MemoryRepository
from .use_cases.room_list import room_list_use_case


repo = MemoryRepository([])
room_list_use_case(repo)

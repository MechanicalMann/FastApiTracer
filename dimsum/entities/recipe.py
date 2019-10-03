from dataclasses import dataclass, field


@dataclass
class Recipe(object):
    id: str
    name: str
    description: str = None
    total_time: int = 0
    total_time_reviewed: bool = False

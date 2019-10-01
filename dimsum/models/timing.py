from pydantic import BaseModel


class Timing(BaseModel):
    total_time: int = 0
    total_time_reviewed: bool = False

from pydantic import BaseModel

from dimsum.models.timing import Timing


class Recipe(BaseModel):
    id: str = None
    name: str
    description: str = ""
    timing: Timing = Timing()

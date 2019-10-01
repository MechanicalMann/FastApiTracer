from pydantic import BaseModel

from dimsum.models.timing import Timing


class Recipe(BaseModel):
    id: str
    name: str
    description: str = ""
    timing: Timing = Timing()

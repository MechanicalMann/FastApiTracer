from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator

app = FastAPI()


class TimingModel(BaseModel):
    prep_time: int = 0
    cook_time: int = 0
    total_time: int = 0
    total_time_reviewed: bool = False

    @validator('total_time')
    def validate_total_time(cls, v):
        if v < 1:
            raise ValueError('Total time must be greater than 0')
        return v


class Recipe(BaseModel):
    id: str
    name: str
    description: str = None
    timing: TimingModel = TimingModel()


@app.get('/')
async def root():
    return {'message': 'Hello world!'}


@app.get('/recipes/{id}')
async def get_recipe(id: str):
    return Recipe(id=id, name='Test recipe', timing=TimingModel())


@app.post('/recipes')
async def post_recipe(recipe: Recipe):
    return 'Ok!'
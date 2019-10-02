from fastapi import FastAPI

from dimsum.endpoints import recipies

api = FastAPI()
api.include_router(recipies.router)

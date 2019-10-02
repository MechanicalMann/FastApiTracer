from fastapi import FastAPI

from dimsum.endpoints import recipes

api = FastAPI()
api.include_router(recipes.router)

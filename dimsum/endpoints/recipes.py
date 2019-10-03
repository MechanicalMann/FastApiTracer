from fastapi import APIRouter

from dimsum import responses
from dimsum.models.recipe import Recipe
from dimsum.repositories.recipe import RecipeRepository

router = APIRouter()
recipes = RecipeRepository()


@router.get('/recipes')
async def get_recipes():
    return []


@router.get('/recipes/{id}')
async def get_recipe(id: str):
    recipe = recipes.get_recipe(id)
    if not recipe:
        return responses.not_found({'message': 'No recipe found with that ID'})
    return recipe


@router.post('/recipes')
async def post_recipe(recipe: Recipe):
    recipes.add_recipe(recipe)

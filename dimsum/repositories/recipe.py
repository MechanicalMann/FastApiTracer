import uuid

from google.cloud import firestore

from dimsum.models.recipe import Recipe
from dimsum.models.timing import Timing


class RecipeRepository(object):
    def __init__(self):
        self._db = firestore.Client()

    def get_recipes(self):
        return []

    def get_recipe(self, id: str):
        docref = self._db.collection('mm-test').document(id)
        doc = docref.get()
        if not doc.exists:
            return None
        return self._map_to_model(doc.id, doc.to_dict())

    def add_recipe(self, recipe: Recipe):
        if not recipe.id:
            recipe.id = uuid.uuid4()
        values = self._map_from_model(recipe)
        self._db.collection('mm-test').document(recipe.id).set(values)
        return recipe.id

    def _map_to_model(self, id, source):
        return Recipe(
            id=id,
            name=source['name'],
            description=source['description'],
            timing=Timing(
                total_time=source['derived_total_time'],
                total_time_reviewed=source['derived_total_time_reviewed']))

    def _map_from_model(self, model: Recipe):
        return {
            'name': model.name,
            'description': model.description,
            'derived_total_time': model.timing.total_time,
            'derived_total_time_reviewed': model.timing.total_time_reviewed
        }

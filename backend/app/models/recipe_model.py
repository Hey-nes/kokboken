from typing import List, TypedDict, Optional

class RecipeIngredient(TypedDict):
    ingredient_name: str
    amount: float
    unit: str

class RecipeCreate(TypedDict):
    title: str
    cooking_duration: int
    portion: int
    category: str
    ingredients: List[RecipeIngredient]
    recipe_steps: List[str]
    picture: Optional[str]

class RecipeStep(TypedDict):
    step_number: int
    instruction: str
from pydantic import BaseModel, Field
from typing import List, Optional, Literal


class RecipeIngredient(BaseModel):
    ingredient_name: str
    amount: float = Field(gt=0)
    unit: Literal["kg", "g", "l", "dl", "ml", "msk", "tsk", "krm", "stk"]


class RecipeStep(BaseModel):
    step_number: int = Field(gt=0)
    instruction: str = Field(min_length=1, max_length=200)


CategoryType = Literal[
    "breakfast", "lunch", "dinner", "dessert", "meat", "fish", "vegetarian", "vegan"
]


class RecipeCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    cooking_duration: int = Field(gt=0)
    portion: int = Field(gt=0)
    category: CategoryType
    ingredients: List[RecipeIngredient]
    recipe_steps: List[str]
    picture: Optional[str] = None


class RecipeUpdate(BaseModel):
    title: Optional[str] = None
    cooking_duration: Optional[int] = None
    portion: Optional[int] = None
    category: Optional[CategoryType] = None
    ingredients: Optional[List[RecipeIngredient]] = None
    recipe_steps: Optional[List[str]] = None
    picture: Optional[str] = None

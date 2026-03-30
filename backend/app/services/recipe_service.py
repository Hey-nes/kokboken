from app.repositories import recipe_repo
from app.models import recipe_model
from pydantic import ValidationError


def add_new_recipe(db_connection, data: dict):
    try:
        # Validate input data and convert it to dict
        validated_data = recipe_model.RecipeCreate(**data)
        validated_dict = validated_data.model_dump()

        # Loop through steps, add step number
        validated_dict["recipe_steps"] = [
            {"step_number": index, "instruction": instruction}
            for index, instruction in enumerate(validated_dict["recipe_steps"], start=1)
        ]

        # Pass the completed dict to repo
        return recipe_repo.create_recipe(db_connection, validated_dict)

    except ValidationError as e:
        print(e.json())
        raise ValueError(f"Invalid input data: {e}")

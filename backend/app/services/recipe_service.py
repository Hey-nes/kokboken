from app.repositories import recipe_repo
from app.models import recipe_model
from pydantic import ValidationError


# Helper functions which adds steps to recipes
def _add_steps(data):
    # Loop through steps, add step number
    data["recipe_steps"] = [
        {"step_number": index, "instruction": instruction}
        for index, instruction in enumerate(data["recipe_steps"], start=1)
    ]

    return data


def add_new_recipe(db_connection, data: dict):
    try:
        # Validate input data and convert it to dict
        validated_data = recipe_model.RecipeCreate(**data)
        validated_dict = validated_data.model_dump()

        if validated_dict.get("recipe_steps"):
            _add_steps(validated_dict)

        # Pass the completed dict to repo
        return recipe_repo.create_recipe(db_connection, validated_dict)

    except ValidationError as e:
        raise ValueError(f"Invalid input data: {e}")

    except Exception as e:
        raise ValueError(f"Error processing recipe: {e}")


def get_all_recipes(db_connection):
    return recipe_repo.get_all_recipes(db_connection)


def get_recipe_by_id(db_connection, recipe_id):
    return recipe_repo.get_recipe_by_id(db_connection, recipe_id)


def update_recipe(db_connection, recipe_id, data):
    try:
        # Validate input data and convert it to dict
        validated_data = recipe_model.RecipeUpdate(**data)
        validated_dict = validated_data.model_dump(exclude_unset=True)

        if validated_dict.get("recipe_steps"):
            _add_steps(validated_dict)

        if validated_dict:
            return recipe_repo.update_recipe(db_connection, recipe_id, validated_dict)

    except ValidationError as e:
        raise ValueError(f"Invalid update data: {e}")

    except Exception as e:
        raise ValueError(f"Error updating recipe: {e}")


def delete_recipe(db_connection, recipe_id):
    return recipe_repo.delete_recipe(db_connection, recipe_id)

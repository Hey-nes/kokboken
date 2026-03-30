# Helper function to insert and link ingredients
def _insert_ingredients(data, recipe_id, cursor):

    for ingredient in data["ingredients"]:
        # First insert ingredient into database
        cursor.execute(
            (
                """
                    INSERT IGNORE INTO ingredients (ingredient_name)
                    VALUES (%s)
                    """
            ),
            (ingredient["ingredient_name"],),
        )

        # Fetch ingredient id
        cursor.execute(
            "SELECT id FROM ingredients WHERE ingredient_name = %s",
            (ingredient["ingredient_name"],),
        )
        ingredient_id = cursor.fetchone()[0]

        # Link them together by inserting them into recipe_ingredients
        cursor.execute(
            """
                           INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount, unit)
                           VALUES (%s, %s, %s, %s)
                        """,
            (recipe_id, ingredient_id, ingredient["amount"], ingredient["unit"]),
        )


# Helper function to insert and link steps
def _insert_steps(data, recipe_id, cursor):

    for step in data["recipe_steps"]:
        cursor.execute(
            """
                           INSERT INTO recipe_steps (recipe_id, step_number, instruction)
                           VALUES (%s, %s, %s)
                        """,
            (recipe_id, step["step_number"], step["instruction"]),
        )


def create_recipe(db_connection, data):
    cursor = db_connection.cursor()

    try:
        db_connection.start_transaction()

        recipe_query = """
            INSERT INTO recipes (title, cooking_duration, portion, category, picture)
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            recipe_query,
            (
                data["title"],
                data["cooking_duration"],
                data["portion"],
                data["category"],
                data.get("picture"),
            ),
        )

        recipe_id = cursor.lastrowid

        _insert_ingredients(data, recipe_id, cursor)
        _insert_steps(data, recipe_id, cursor)

        db_connection.commit()
        return recipe_id

    except Exception as e:
        db_connection.rollback()
        raise e

    finally:
        cursor.close()


def get_all_recipes(db_connection):
    cursor = db_connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM recipes")
        recipes = cursor.fetchall()
        return recipes

    except Exception as e:
        raise e

    finally:
        cursor.close()


def get_recipe_by_id(db_connection, recipe_id):
    cursor = db_connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM recipes WHERE id = %s", (recipe_id,))
        recipe = cursor.fetchone()

        # Fetch the recipes ingredients and steps
        if recipe:
            cursor.execute(
                "SELECT ingredients.id, ingredients.ingredient_name, recipe_ingredients.amount, recipe_ingredients.unit FROM recipe_ingredients INNER JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.id WHERE recipe_id = %s",
                (recipe_id,),
            )
            recipe["ingredients"] = cursor.fetchall()

            cursor.execute("SELECT * FROM recipe_steps WHERE recipe_id = %s ORDER BY step_number", (recipe_id,))
            recipe["steps"] = cursor.fetchall()

        return recipe

    except Exception as e:
        raise e

    finally:
        cursor.close()


def update_recipe(db_connection, recipe_id, data):
    cursor = db_connection.cursor()

    try:
        db_connection.start_transaction()
        cursor.execute(
            "UPDATE recipes SET title = %s, cooking_duration = %s, portion = %s, category = %s, picture = %s WHERE id = %s",
            (
                data["title"],
                data["cooking_duration"],
                data["portion"],
                data["category"],
                data.get("picture"),
                recipe_id,
            ),
        )

        if "ingredients" in data:
            cursor.execute(
                "DELETE FROM recipe_ingredients WHERE recipe_id = %s", (recipe_id,)
            )
            _insert_ingredients(data, recipe_id, cursor)

        if "recipe_steps" in data:
            cursor.execute(
                "DELETE FROM recipe_steps WHERE recipe_id = %s", (recipe_id,)
            )
            _insert_steps(data, recipe_id, cursor)

        db_connection.commit()
        return True

    except Exception as e:
        db_connection.rollback()
        raise e

    finally:
        cursor.close()


def delete_recipe(db_connection, recipe_id):
    cursor = db_connection.cursor()

    try:
        cursor.execute("DELETE FROM recipes WHERE id = %s", (recipe_id,))
        db_connection.commit()
        return cursor.rowcount > 0

    except Exception as e:
        db_connection.rollback()
        raise e

    finally:
        cursor.close()

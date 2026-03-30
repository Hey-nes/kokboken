def create_recipe(db_connection, validated_dict):
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
                validated_dict["title"],
                validated_dict["cooking_duration"],
                validated_dict["portion"],
                validated_dict["category"],
                validated_dict.get("picture"),
            ),
        )

        recipe_id = cursor.lastrowid

        # Insert and link ingredients in database
        for ingredient in validated_dict["ingredients"]:
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

            # Fetch ingredientid
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

        for step in validated_dict["recipe_steps"]:
            cursor.execute(
                """
                           INSERT INTO recipe_steps (recipe_id, step_number, instruction)
                           VALUES (%s, %s, %s)
                        """,
                (recipe_id, step["step_number"], step["instruction"]),
            )

        db_connection.commit()
        return recipe_id

    except Exception as e:
        db_connection.rollback()
        raise e

    finally:
        cursor.close()

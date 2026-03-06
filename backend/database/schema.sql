CREATE DATABASE IF NOT EXISTS kokboken_db;
USE kokboken_db;

CREATE TABLE IF NOT EXISTS recipes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  cooking_duration INT NOT NULL,
  portion INT NOT NULL CHECK (portion > 0),
  category ENUM("breakfast", "lunch", "dinner", "dessert", "meat", "fish", "vegetarian", "vegan") NOT NULL,
  picture VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS ingredients (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ingredient_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS recipe_ingredients (
  id INT AUTO_INCREMENT PRIMARY KEY,
  recipe_id INT NOT NULL,
  ingredient_id INT NOT NULL,
  amount FLOAT NOT NULL CHECK (amount > 0),
  unit ENUM("kg", "g", "l", "dl", "ml", "msk", "tsk", "krm") NOT NULL,
  CONSTRAINT fk_recipe_ingredients FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
  CONSTRAINT fk_ingredient FOREIGN KEY (ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS recipe_steps (
  id INT AUTO_INCREMENT PRIMARY KEY,
  recipe_id INT NOT NULL,
  step_number INT NOT NULL,
  instruction TEXT NOT NULL,
  CONSTRAINT fk_recipe_steps FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
  CONSTRAINT UNIQUE (recipe_id, step_number)
);
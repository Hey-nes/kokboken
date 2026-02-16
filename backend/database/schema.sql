CREATE DATABASE IF NOT EXISTS kokboken_db;
USE kokboken_db;

CREATE TABLE recipies (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  time VARCHAR(50) NOT NULL,
  portion INT NOT NULL CHECK (portion > 0),
  category ENUM("breakfast", "lunch", "dinner", "dessert") NOT NULL,
  picture VARCHAR(255)
);

CREATE TABLE recipie_ingredients (
  id INT AUTO_INCREMENT PRIMARY KEY,
  recipie_id INT NOT NULL,
  ingredient_name VARCHAR(100) NOT NULL,
  amount FLOAT NOT NULL CHECK (amount > 0),
  unit ENUM("l", "dl", "msk", "tsk", "krm") NOT NULL,
  CONSTRAINT fk_recipie_ingredients FOREIGN KEY (recipie_id) REFERENCES recipies(id) ON DELETE CASCADE
);

CREATE TABLE recipie_method (
  id INT AUTO_INCREMENT PRIMARY KEY,
  recipie_id INT NOT NULL,
  step_order INT NOT NULL,
  instruction TEXT NOT NULL,
  CONSTRAINT fk_recipie_method FOREIGN KEY (recipie_id) REFERENCES recipies(id) ON DELETE CASCADE
);
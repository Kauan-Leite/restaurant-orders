import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        data = pd.read_csv(source_path)
        self.dishes = set()

        for dish, price in data[["dish", "price"]].itertuples(index=False):
            self.dishes.add(Dish(dish, price))

        for dish, ingredient, recipe_amount in data[
            ["dish", "ingredient", "recipe_amount"]
                ].itertuples(index=False):
            for item in self.dishes:
                if item.name == dish:
                    item.add_ingredient_dependency(
                        Ingredient(ingredient), recipe_amount
                        )

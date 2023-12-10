"""
Cooking serive API

This module contains the CookingService class, which is a service for checking and cooking recipes based on available inventory.
"""

from inventory_app.inventory import Inventory
from inventory_app.recipe import Recipe


class CookingException(Exception):
    """Exception raised for an error during cooking."""


class CookingService:
    """A service for checking and cooking recipes based on available inventory."""

    def is_cookable(self, recipe: Recipe, inventory: Inventory):
        """
        Check if the given recipe can be prepared based on the available inventory.

        Args:
            recipe (Recipe): The recipe to be checked.
            inventory (Inventory): The inventory of ingredients.

        Returns:
            bool: True if the recipe can be prepared, False otherwise.
        """
        for ingredient, quantity in recipe.ingredients.items():
            if ingredient not in inventory or inventory[ingredient] < quantity:
                return False
        return True

    def cook_recipe(self, recipe: Recipe, inventory: Inventory):
        """
        Cooks a recipe using the provided inventory.

        Args:
            recipe (Recipe): The recipe to be cooked.
            inventory (Inventory): The inventory containing the ingredients.

        Raises:
            CookingException: If there are not enough ingredients to cook the recipe.
        """

        if not self.is_cookable(recipe, inventory):
            raise CookingException("Not enough ingredients to cook the recipe")

        for ingredient, quantity in recipe.ingredients.items():
            inventory[ingredient] -= quantity
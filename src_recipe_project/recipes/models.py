from django.db import models

# Create Recipe model
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooking_time = models.PositiveIntegerField(help_text='In minutes')
    description = models.TextField(default='No description yet...')
    difficulty = models.CharField(max_length=27, default='Difficulty not yet rated...')
    ingredients = models.ManyToManyField(
        'ingredients.Ingredient', through='recipeingredients.RecipeIngredient'
    )

    def calculate_difficulty(self):
        from recipeingredients.models import (RecipeIngredient)
        num_ingredients = RecipeIngredient.objects.filter(recipe=self).count()
        cooking_time = self.cooking_time

        if cooking_time < 10 and num_ingredients < 4:
            return 'Easy'
        elif cooking_time < 10 and num_ingredients >= 4:
            return 'Medium'
        elif cooking_time >= 10 and num_ingredients < 4:
            return 'Intermediate'
        else:
            return 'Hard'

    def save(self, *args, **kwargs):
        self.difficulty = self.calculate_difficulty()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


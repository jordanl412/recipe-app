from django.test import TestCase
from .models import Recipe
from recipeingredients.models import RecipeIngredient
from ingredients.models import Ingredient
from .forms import RecipeSearchForm
from django.contrib.auth.models import User

# Create your tests here.
class RecipeModelTest(TestCase):
    # Test for recipe string representation
    def test_recipe_string_representation(self):
        #  Create a recipe object to test
        recipe = Recipe.objects.create(
            name='Test Recipe', cooking_time=30, description='Test description'
        )
        # Compare string representations
        self.assertEqual(str(recipe), 'Test Recipe')

    # Test for recipe difficulty (easy)
    def test_recipe_easy_difficulty(self):
        # Create a recipe object to test
        recipe = Recipe.objects.create(
            name='Test Recipe', cooking_time=5, description='Test description'
        )
        # Add 2 ingredients to make recipe Easy difficulty
        ingredient1 = Ingredient.objects.create(name='Ingredient 1')
        ingredient2 = Ingredient.objects.create(name='Ingredient 2')
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient1)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient2)
        # Update recipe difficulty
        recipe.save()
        # Compare recipe difficulties
        self.assertEqual(recipe.difficulty, 'Easy')

    # Test for recipe difficulty (medium)
    def test_recipe_medium_difficulty(self):
        # Create a recipe object to test
        recipe = Recipe.objects.create(
            name='Test Recipe', cooking_time=5, description='Test description'
        )
        # Add 5 ingredients to make recipe Medium difficulty
        ingredient1 = Ingredient.objects.create(name='Ingredient 1')
        ingredient2 = Ingredient.objects.create(name='Ingredient 2')
        ingredient3 = Ingredient.objects.create(name='Ingredient 3')
        ingredient4 = Ingredient.objects.create(name='Ingredient 4')
        ingredient5 = Ingredient.objects.create(name='Ingredient 5')
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient1)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient2)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient3)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient4)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient5)
        # Update recipe difficulty
        recipe.save()
        # Compare recipe difficulties
        self.assertEqual(recipe.difficulty, 'Medium')

    # Test for recipe difficulty (intermediate)
    def test_recipe_intermediate_difficulty(self):
        # Create a recipe object to test
        recipe = Recipe.objects.create(
            name='Test Recipe', cooking_time=30, description='Test description'
        )
        # Add 2 ingredients to make recipe Intermediate difficulty
        ingredient1 = Ingredient.objects.create(name='Ingredient 1')
        ingredient2 = Ingredient.objects.create(name='Ingredient 2')
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient1)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient2)
        # Update recipe difficulty
        recipe.save()
        # Compare recipe difficulties
        self.assertEqual(recipe.difficulty, 'Intermediate')

    # Test for recipe difficulty (hard)
    def test_recipe_hard_difficulty(self):
        # Create a recipe object to test
        recipe = Recipe.objects.create(
            name='Test Recipe', cooking_time=30, description='Test description'
        )
        # Add 5 ingredients to make recipe Hard difficulty
        ingredient1 = Ingredient.objects.create(name='Ingredient 1')
        ingredient2 = Ingredient.objects.create(name='Ingredient 2')
        ingredient3 = Ingredient.objects.create(name='Ingredient 3')
        ingredient4 = Ingredient.objects.create(name='Ingredient 4')
        ingredient5 = Ingredient.objects.create(name='Ingredient 5')
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient1)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient2)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient3)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient4)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient5)
        # Update recipe difficulty
        recipe.save()
        # Compare recipe difficulties
        self.assertEqual(recipe.difficulty, 'Hard')

    # Test get_absolute_url
    def test_get_absolute_url(self):
        recipe = Recipe.objects.create(
            id=1, name='Test Recipe', cooking_time=30, description='Test description'
        )
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    # Test RecipesListView
    def test_recipes_list_view(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')
    
    # Test RecipesDetailView
    def test_recipes_detail_view(self):
        recipe = Recipe.objects.create(
            id=1, name='Test Recipe', cooking_time=30, description='Test description'
        )
        response = self.client.get('/list/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_detail.html')

    def setUp(self):
        # Create a test user and log them in for the view requiring login
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_view_protected(self):
       self.client.logout()
       response = self.client.get('/recipes/')
       self.assertEqual(response.status_code, 302)
       self.assertRedirects(response, '/login/?next=/recipes/') 

    def test_form_validation_with_valid_data(self):
        form = RecipeSearchForm({'recipe_category': 'Breakfast', 'chart_type': 'Bar Chart'})
        self.assertTrue(form.is_valid())


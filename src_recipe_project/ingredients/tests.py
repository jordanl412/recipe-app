from django.test import TestCase
# To access Ingredients model
from .models import Ingredient

# Create your tests here.
class IngredientModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Ingredient.objects.create(name='Bread')

    # Test for ingredient name
    def test_ingredient_name(self):
        # Get an ingredient object to test
        ingredient = Ingredient.objects.get(id=1)
        # Get the metadata for the 'name' field and use it to query its data
        field_label = ingredient._meta.get_field('name').verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    # Test for ingredient name max length
    def test_ingredient_name_max_length(self):
        # Get an ingredient object to test
        ingredient = Ingredient.objects.get(id=1)
        # Get the metadata for the 'name' field and use it to query its data
        max_length = ingredient._meta.get_field('name').max_length
        # Compare it to the expected result (255)
        self.assertEqual(max_length, 255)

    # Test for ingredient string representation
    def test_ingredient_string_representation(self):
        # Get an ingredient object to test
        ingredient = Ingredient.objects.get(id=1)
        # Compare string representations
        self.assertEqual(str(ingredient), 'Bread')



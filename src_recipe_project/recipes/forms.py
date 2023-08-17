from django import forms

RECIPE_CATEGORY_CHOICES = (
    ('Drink', 'Drink'),
    ('Breakfast', 'Breakfast'),
    ('Lunch/Dinner', 'Lunch/Dinner'),
    ('Dessert', 'Dessert'),
    ('Show All', 'Show All'),
)

CHART_CHOICES = (
    ('Bar Chart', 'Bar Chart'),
    ('Pie Chart', 'Pie Chart'),
    ('Line Chart', 'Line Chart'),
)

class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(
        max_length=255,
        required=False,
        label='Recipe Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter a Recipe Name'}
        ),
    )
    recipe_category = forms.ChoiceField(
        choices=RECIPE_CATEGORY_CHOICES,
        required=False,
        label='Category',
        )
    ''' For later integration
    ingredients = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Ingredients.objects.all(),
        label='Ingredient(s)',
    )
    '''
    chart_choice = forms.ChoiceField(
        choices=CHART_CHOICES,
        required=False,
        label='Chart Type'
    )

    def clean(self):
        cleaned_data = super().clean()
        recipe_name = cleaned_data.get('recipe_name')
        recipe_category = cleaned_data.get('recipe_category')
        # ingredients = cleaned_data.get('ingredients')

        if not recipe_name and not recipe_category:
            raise forms.ValidationError(
                'Please enter a recipe name or select a recipe category.'
            )
        return cleaned_data

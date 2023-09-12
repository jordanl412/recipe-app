from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm, createRecipeForm
from .utils import get_recipename_from_id, get_chart
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'

@login_required
def records(request):
    # Create instance of RecipeSearchForm that is defined in recipes/forms.py
    form = RecipeSearchForm(request.GET or None)
    # Initialize dataframe to None
    recipes_df = None
    chart = None
    # Check if button is clicked
    if form.is_valid():
        name = form.cleaned_data.get('recipe_name')
        category = form.cleaned_data.get('recipe_category')
        chart_type = form.cleaned_data.get('chart_choice')
        if category == 'Show All':
            qs = Recipe.objects
        elif name and category:
            qs = Recipe.objects.filter(name__icontains=name, category__icontains=category)
        elif name:
            qs = Recipe.objects.filter(name__icontains=name)
        elif category:
            qs = Recipe.objects.filter(category__icontains=category)
        if qs:
            # Convert QuerySet values to pandas dataframe
            recipes_df = pd.DataFrame(qs.values())
            print('recipes_df:', recipes_df)
            # Convert ID to recipename
            #recipes_df['recipe_id'] = recipes_df['recipe_id'].apply(get_recipename_from_id)
            # Call get_chart by passing chart_type from user input, recipe dataframe and labels
            chart = get_chart(chart_type, recipes_df, labels=recipes_df.values)
            # Convert the dataframe to HTML
            recipes_df = recipes_df.to_html()
        # Display in terminal for debugging and dev only
        print(recipes_df, chart_type)

    # Data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart,
    }

    # Load the recipes/record.html page using the above prepared data
    return render(request, 'recipes/records.html', context)

@login_required
def about(request):
    return render(request, 'recipes/about.html')

@login_required
def create(request):
    create_form = createRecipeForm(request.POST or None, request.FILES)
    name = None
    cooking_time = None
    category = None
    ingredients = None
    description = None

    if request.method == 'POST':
        try:
            recipe = Recipe.objects.create(
                name = request.POST.get('name'),
                cooking_time = request.POST.get('cooking_time'),
                category = request.POST.get('category'),
                ingredients = request.POST.get('ingredients'),
                description = request.POST.get('description'),
            )

            recipe.save()

        except:
            print('An error has occurred')

    context = {
        'create_form': create_form,
        'name': name,
        'cooking_time': cooking_time,
        'category': category,
        'ingredients': ingredients,
        'description': description,
        }

    return render(request, 'recipes/create.html', context)

'''
@login_required
def records(request):
    # Create instance of RecipeSearchForm that is defined in recipes/forms.py
    form = RecipeSearchForm(request.GET or None)
    # Initialize dataframe to None
    recipes = None
    # Check if button is clicked
    if form.is_valid():
        name = form.cleaned_data.get('recipe_name')
        category = form.cleaned_data.get('recipe_category')
        if name and category:
            recipes = Recipe.objects.filter(name__icontains=name, category__icontains=category)
        elif name:
            recipes = Recipe.objects.filter(name__icontains=name)
        elif category:
            recipes = Recipe.objects.filter(category__icontains=category)
    return render(request, 'recipes/records.html', {'form': form, 'recipes_df': recipes})
'''

'''
@login_required
def records(request):
    # Create instance of RecipeSearchForm that is defined in recipes/forms.py
    form = RecipeSearchForm(request.POST or None)
    # Initialize dataframe to None
    recipes_df = None
    chart = None

    # Check if button is clicked
    if request.method == 'POST':
        # Read form elements
        recipe_name = request.POST.get('recipe_name')
        recipe_category = request.POST.get('recipe_category')
        # For later integration
        # ingredients = request.POST.get('ingredients')
        chart_type = request.POST.get('chart_type')

        # Filter Recipe objects based on the request
        # qs is QuerySet
        if recipe_name and not recipe_category:
            qs = Recipe.objects.filter(name=recipe_name)

        elif recipe_category and not recipe_name:
            qs = Recipe.objects.filter(category=recipe_category)

        elif recipe_name and recipe_category:
            qs = Recipe.objects.filter(name=recipe_name, category=recipe_category)

        # For later implementation
        # if ingredients:
        #    for ingredient in ingredients:
        #       qs = qs.filter(ingredients__id=ingredient)
       


        if qs:
            # Convert QuerySet values to pandas dataframe
            recipes_df = pd.DataFrame(qs.values())
            print('recipes_df:', recipes_df)
            # Convert ID to recipename
            recipes_df['recipe_id'] = recipes_df['recipe_id'].apply(get_recipename_from_id)
            # Call get_chart by passing chart_type from user input, recipe dataframe and labels
            chart = get_chart(chart_type, recipes_df, labels=recipes_df['recipe_id'].values)
            # Convert the dataframe to HTML
            recipes_df = recipes_df.to_html()
        # Display in terminal for debugging and dev only
        print(recipe_name, chart_type)

    # Data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart,
    }

    # Load the recipes/record.html page using the above prepared data
    return render(request, 'recipes/records.html', context)
    '''
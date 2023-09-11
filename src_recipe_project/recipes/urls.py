from django.urls import path
from .views import (
    home,
    RecipeListView,
    RecipeDetailView,
    records,
    about,
)

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', RecipeListView.as_view(), name='recipes_list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='recipes_detail'),
    path('recipes/records', records, name='records'),
    path('about/', about, name='about'),
]


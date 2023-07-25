from django.urls import path
from .views import home, RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipeListView.as_view(), name='recipes_list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='recipes_detail'),
]


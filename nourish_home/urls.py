# from django.urls import path
# from .views import home_page_view

# urlpatterns = [
#     path('', home_page_view)
# ]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),

]
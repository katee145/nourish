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
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),

]
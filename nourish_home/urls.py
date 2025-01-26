from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

"""
Defines URL patterns for nourish_home.
"""

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.RecipeDetailView.as_view(),
         name='recipe_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('', views.RecipeList.as_view(), name='recipe_list'),
    path('accounts/login/', auth_views.LoginView.as_view(),
         name='login'),
]


# Register the custom 404 handler (corrected syntax)
handler404 = 'nourish_home.views.handler404'

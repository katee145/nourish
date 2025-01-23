from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.db.models.signals import post_migrate
from django.apps import apps
from .models import Recipe, Comment, Category

"""
Predefined Categories:
    - Create predefined categories upon app migration.
    - Defines a list of predefined category names.
    - Creates a category if it doens't exist.
"""


def create_predefined_categories(sender, **kwargs):
    # List of predefined categories
    categories = [
        'Budget eats', 'Under 30 mins', 'Wow your guests',
        'Breakfast', 'Lunch', 'Dinner',
        'Gluten free', 'Vegetarian', 'Vegan',
        'Meat', 'Fish', 'Protein-focused', 'Prep ahead'
    ]
    # Creates a category if it doesn't exist
    for category_name in categories:
        Category.objects.get_or_create(name=category_name)


post_migrate.connect(
    create_predefined_categories, sender=apps.get_app_config('nourish_home'))


"""
Recipe Admin:
    - Inherits from `SummernoteModelAdmin` for rich text editing.
    - Configures the admin interface for the `Recipe` model.
    - `list_display`: Defines fields to display in the recipe list view.
    - `search_fields`: Specifies fields to search when searching for recipes.
    - `list_filter`: Enables filtering recipes by status in the admin view.
    - `prepopulated_fields`: Auto populates 'slug' based on the 'title'.
    - `summernote_fields`: Enables rich text editing for the 'description'.
    - `filter_horizontal`: Allows selecting multiple categories.
"""


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'slug', 'status')
    search_fields = ['title', 'ingredients', 'description', 'instructions']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
    filter_horizontal = ('categories',)


"""
Category Admin:
    - `CategoryAdmin` class inherits from `admin.ModelAdmin`.
    - Configures the admin interface for the `Category` model.
    - `list_display`: Defines fields to display in the category list view.
"""


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


"""
Registers the `Comment` model with the admin site.
"""


admin.site.register(Comment)

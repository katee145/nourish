from django.contrib import admin
from .models import Recipe, Comment, Category
from django_summernote.admin import SummernoteModelAdmin
from django.db.models.signals import post_migrate
from django.apps import apps

def create_predefined_categories(sender, **kwargs):
    # List of predefined categories
    categories = ['Budget eats', 'Under 30 mins', 'Wow your guests', 'Breakfast', 'Lunch', 'Dinner', 'Gluten free', 'Vegetarian', 'Vegan', 'Meat', 'Fish', 'Protein-focused', 'Prep ahead']
    
    # Creates a category if it doesn't exist
    for category_name in categories:
        Category.objects.get_or_create(name=category_name)

post_migrate.connect(create_predefined_categories, sender=apps.get_app_config('nourish_home'))

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'slug', 'status')
    search_fields = ['title', 'ingredients', 'description', 'instructions']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
    filter_horizontal = ('categories',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Comment)
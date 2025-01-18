from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = (
    (0, 'Draft'), 
    (1, 'Published'),
) 


class Recipe(models.Model):
    """
    Model for recipe.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="recipes"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.ManyToManyField('Ingredient', related_name='recipes', blank=True)  # Added related_name here
    cooking_time = models.IntegerField(default=0)
    prep_time = models.IntegerField(default=0)
    servings = models.PositiveIntegerField(default=1)
    description = models.TextField()
    instructions = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    """
    Model representing a recipe ingredient.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredient_set")  # Changed related_name here
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=50, blank=True)
    unit = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"


class Category(models.Model):
    """
    Model representing a recipe category.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    """
    Many-to-many relationship between Recipe and Category.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Comment(models.Model):
    """
    Model for comments.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"



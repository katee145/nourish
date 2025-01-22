from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = (
    (0, 'Draft'), 
    (1, 'Published'),
) 

class Category(models.Model):
    """
    Model representing a recipe category.
    """
    name = models.CharField(max_length=100, unique=True)
    # safe_name = would act like a slug, remvoe whitespace and lowercase. e.g. Gluten Free = gluten-free

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Model for recipe.
    """
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    categories = models.ManyToManyField(Category, related_name='recipes', blank=False)  # Multiple categories required
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="recipes", blank=False
    )
    featured_image = CloudinaryField('image', default='placeholder', blank=True)  # Image can be left blank
    ingredients = models.TextField(blank=False)  # Ingredients are required
    cooking_time = models.IntegerField(default=0, blank=False)
    prep_time = models.IntegerField(default=0, blank=False)
    servings = models.PositiveIntegerField(default=1, blank=False)
    description = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    status = models.IntegerField(choices=STATUS, default=0, blank=False)

    def __str__(self):
        return self.title


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

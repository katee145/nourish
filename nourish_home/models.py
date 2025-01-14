from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    """
    Model for recipe.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="recipes"
    )
    description = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(default=0)
    prep_time = models.IntegerField(default=0)
    servings = models.PositiveIntegerField(default=1)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
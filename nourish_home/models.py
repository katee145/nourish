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
    Assigns category to recipes.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Model for a single recipe including image and all relevant cooking details.

    """
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    categories = models.ManyToManyField(
        Category, related_name='recipes', blank=False)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="recipes",
        blank=False
    )
    featured_image = CloudinaryField(
        'image', default='placeholder', blank=True)
    ingredients = models.TextField(blank=False)
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
    Model for comments on recipes along with the author and date.
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

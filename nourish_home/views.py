from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views import generic
from .models import Recipe
from .forms import CommentForm

# Create your views here.
class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = "nourish_home/index.html"
    #paginate_by = 6


class RecipeDetailView(View):
    """
    Display an individual :model:`Recipe` with comments and a form to add a comment.
    """
    def get(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug, status=1)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        comment_form = CommentForm()
        return render(request, "recipe_detail.html", {
            "recipe": recipe,
            "comments": comments,
            "comment_form": comment_form,
        })

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug, status=1)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            return redirect("recipe_detail", slug=recipe.slug)
        return render(request, "recipe_detail.html", {
            "recipe": recipe,
            "comments": comments,
            "comment_form": comment_form,
        })
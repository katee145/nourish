from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Recipe, Comment, Category
from .forms import CommentForm


# Views below
class RecipeList(generic.ListView):
    """
    Displays a list of recipes with pagination.
    """
    model = Recipe
    template_name = "nourish_home/index.html"
    paginate_by = 8

    def get_queryset(self):
        """
        Refines recipe list based on search.
        """
        queryset = super().get_queryset()
        category_slug = self.request.GET.get('category')
        search_query = self.request.GET.get('search')
        if category_slug:
            queryset = queryset.filter(categories__name=category_slug)
        # Search Query Logic.
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(categories__name__icontains=search_query) |
                Q(ingredients__icontains=search_query)
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class RecipeDetailView(View):
    """
    Display an individual recipe with comments and a form to add a comment.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Retrieves the recipe, approved comments, and comment form.
        """
        recipe = get_object_or_404(Recipe, slug=slug, status=1)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        comment_form = CommentForm()

        # Process ingredients and instructions
        ingredients = (
            recipe.ingredients.splitlines()
            if recipe.ingredients
            else []
        )
        instructions = (
            recipe.instructions.splitlines()
            if recipe.instructions
            else []
        )

        return render(request, "recipe_detail.html", {
            "recipe": recipe,
            "comments": comments,
            "comment_form": comment_form,
            "ingredients": ingredients,
            "instructions": instructions,
        })

    def post(self, request, slug, *args, **kwargs):
        """
        Handles comment submission.
        """
        recipe = get_object_or_404(Recipe, slug=slug, status=1)
        if request.method == "POST":
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.recipe = recipe
                comment.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Comment submitted and awaiting approval'
                )
                return redirect("recipe_detail", slug=recipe.slug)
        return render(request, "recipe_detail.html", {
            "recipe": recipe,
            "comments":
                recipe.comments.filter(approved=True).order_by('created_on'),
            "comment_form": comment_form,
        })


def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    recipe = get_object_or_404(Recipe, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment_form = CommentForm(data=request.POST, instance=comment)

    if request.method == "POST":
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete a comment
    """
    recipe = get_object_or_404(Recipe, slug=slug, status=1)

    if not comment_id:
        return redirect('recipe_detail', slug=slug)

    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def handler404(request, exception):
    """
    Custom 404 error handler.

    This view will be used for all 404 errors.
    """
    return render(request, '404.html', status=404)


def about(request):
    """
    View for the About page.
    """
    context = {
        'about_url': reverse('about'),
    }

    return render(request, 'about.html')

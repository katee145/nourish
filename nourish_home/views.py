from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm


# Create your views here.
class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = "nourish_home/index.html"
    #paginate_by = 6


class RecipeDetailView(View):
    """
    Display an individual :model:Recipe with comments and a form to add a comment.
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

    # def post(self, request, slug, *args, **kwargs):
    #     recipe = get_object_or_404(Recipe, slug=slug, status=1)
    #     comments = recipe.comments.filter(approved=True).order_by('created_on')
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         comment.recipe = recipe
    #         comment.author = request.user
    #         comment.save()
    #         return redirect("recipe_detail", slug=recipe.slug)
    #     return render(request, "recipe_detail.html", {
    #         "recipe": recipe,
    #         "comments": comments,
    #         "comment_form": comment_form,
    #     })

    def post(self, request, slug, *args, **kwargs):
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
            "comments": recipe.comments.filter(approved=True).order_by('created_on'),
            "comment_form": comment_form,
        })

def comment_edit(request, slug, comment_id):
    #view to edit comments
        if request.method == "POST":

            queryset = recipe.objects.filter(status=1)
            recipe = get_object_or_404(queryset, slug=slug)
            comment = get_object_or_404(Comment, pk=comment_id)
            comment_form = CommentForm(data=request.POST, instance=comment)

            if comment_form.is_valid() and comment.author == request.user:
                comment = comment_form.save(commit=False)
                comment.recipe = recipe
                comment.approved = False
                comment.save()
                messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            else:
                messages.add_message(request, messages.ERROR, 'Error updating comment!')

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))

#    def comment_edit(request, slug, comment_id):
#     """
#     Handle editing a comment on a recipe.
#     """
#     recipe = get_object_or_404(Recipe, slug=slug, status=1)
#     comment = get_object_or_404(Comment, pk=comment_id)

#     if comment.author != request.user:
#         messages.error(request, "You are not authorized to edit this comment.")
#         return redirect("recipe_detail", slug=slug)

#     if request.method == "POST":
#         comment_form = CommentForm(data=request.POST, instance=comment)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.recipe = recipe
#             comment.approved = False  # Approval required after editing
#             comment.save()
#             messages.success(request, "Comment updated and awaiting approval.")
#             return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
#     else:
#         comment_form = CommentForm(instance=comment)

#     return render(request, "comment_edit.html", {
#         "recipe": recipe,
#         "comment_form": comment_form,
#     })
from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title','content']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)

# Customizing Comment Admin to display additional information and provide more control
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('recipe', 'author', 'created_on', 'approved')
#     search_fields = ['author__username', 'body']
#     list_filter = ('approved', 'created_on')
#     actions = ['approve_comments', 'disapprove_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)
#     approve_comments.short_description = 'Approve selected comments'

#     def disapprove_comments(self, request, queryset):
#         queryset.update(approved=False)
#     disapprove_comments.short_description = 'Disapprove selected comments'
from django import forms
from .models import Comment

"""
Defines a form for creating and editing comments.

Specifies the model and fields for the form.
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

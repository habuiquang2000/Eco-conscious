from django import forms
from .models import Comment
from ckeditor.fields import RichTextField


class CommentForm(forms.ModelForm):
    description = RichTextField()

    class Meta:
        model = Comment
        fields = ('content', )

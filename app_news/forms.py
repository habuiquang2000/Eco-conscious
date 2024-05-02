from django import forms
from .models.blog import BlogComment
from ckeditor.fields import RichTextField


class CommentForm(forms.ModelForm):
    description = RichTextField()

    class Meta:
        model = BlogComment
        fields = ('content', )

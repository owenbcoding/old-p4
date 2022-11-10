from .models import Comment, Post
from django.utils.translation import gettext_lazy as _
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': _(''),
        }


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'featured_image', 'excerpt')
        lables = {
            'title': _(''), 'slug': _(''), 'content': _(''), 'featured_image': _(''), 'excerpt': _(''),
        }
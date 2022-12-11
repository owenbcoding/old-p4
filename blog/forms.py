from .models import Comment, Post, Contact
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


class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email_address', 'body')
        lables = {
            'first_name': _('test'), 'last_name': _(''), 'email_address': _(''), 'body': _(''),
        }
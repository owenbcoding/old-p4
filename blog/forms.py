from .models import Comment
from django.utils.translation import gettext_lazy as _
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': _(''),
        }
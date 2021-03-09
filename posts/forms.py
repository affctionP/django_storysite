from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=['title','text','published_date','slug']

    """def save(self):
        post_form=super().save(commit=False)
        post_form.author=User.username
        post_form.save()"""
class CommentForm(forms.ModelForm):


    class Meta:
        model=Comment
        fields=('body',)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,reverse,get_object_or_404
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import *
from django.contrib.auth import login
from django.contrib import auth


class PostView(CreateView):
    model=PostModel
    template_name = 'new_post.html'
    form_class = PostForm

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.author=self.request.user
        self.object.save()
        return redirect('accounts:dashboard')

# Create your views here.

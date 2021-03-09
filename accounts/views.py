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

# Create your views here.
class SignView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup_form.html'

    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return redirect('accounts:dashboard')


def ProfileView(request):
    if request.method == 'POST':
        p_form=ProfileForm(request.POST,instance=request.user)
        if p_form.is_valid():
            request.user.bio=p_form.cleaned_data['bio']
            if request.FILES.get('avatar',None) !=None:
                try:
                    os.remove(request.user.avatar.url)
                except Exception as e:
                    print('exception',e)
                request.user.avatar =request.FILES['avatar']
                request.user.save()
            return  render(request,'dashboard.html')
    else:
        p_form=ProfileForm(instance=request.user)
    return render(request,'profile.html',{'form':p_form,'section':'profile'})


def dashboardView(request):
    section='dashboard'
    return render(request,'dashboard.html',{'section':section})





class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '$/dashboard/'
    def form_valid(self, form):
        user=auth.authenticate(self.request,
            username=form.cleaned_data['user_name'],
                               password=form.cleaned_data['password'])
        if user is not None:
            login(self.request,user)
            return super().form_valid(form)
        else:
            return HttpResponse("notmatch")


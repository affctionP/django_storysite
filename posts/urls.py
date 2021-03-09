from django.urls import path,include
from .views import *
from django.conf.urls import url
from django.contrib.auth import views as auth_views
app_name='posts'
urlpatterns=[
url(r'write/$',PostView.as_view(),name='posting'),
        ]
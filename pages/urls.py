from django.urls import path,include
from .views import *
app_name="pages"
urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('post/<int:post_id>',PostDetial,name='post_detail'),

]
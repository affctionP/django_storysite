from .views import *
from django.conf.urls import url
from django.contrib.auth import views as auth_views
app_name="accounts"
urlpatterns=[
    url(r'signup/$',SignView.as_view(),name='signup'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url('profile', ProfileView, name='profile'),
    url('dashboard',dashboardView,name='dashboard'),
    url('logout', auth_views.LogoutView.as_view(template_name="logged_out.html"), name="logout"),
    #++++++++++password reset+++++++++++++++++++++++++++
    url('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url('reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url('password/complete',
        auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
    )


urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^profile/$', views.view_profile, name="profile"),
    url(r'^profile/edit/$', views.edit_profile, name="edit_profile"),
    url(r'^profile/password/$', views.change_password, name="password"),
    url(r'^reset_password/$', PasswordResetView.as_view(), name="reset_password"),
    url(r'^reset_password/done$', PasswordResetDoneView.as_view(), name="password_reset_done"),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset_password/complete$', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

# (?P<uidb64>[0-9A-Za-Z]+)-(?P<token>.+)/

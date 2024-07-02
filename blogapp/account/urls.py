from django.urls import path
from . import views

urlpatterns = [
    path("login",views.login_request, name="login"),
    path("register",views.legister_request, name="register"),
    path("logout",views.logout_request, name="logout"),
]

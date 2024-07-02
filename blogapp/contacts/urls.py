from django.urls import path
from . import views
urlpatterns = [
    path("form", views.form_request, name="form"),
    path("success", views.success, name="success"),
]
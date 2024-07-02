from django.urls import path, include
from . import views
# Sayfa linkleri tanımlanmıştır
urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs,name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category" ),
    path("blogs/<slug:slug>", views.blog_details,name="blog_details"),
    path("contact", views.contact,name="contact"),
    path("about", views.about, name="about"),


]

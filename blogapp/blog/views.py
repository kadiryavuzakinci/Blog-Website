from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog
from blog.models import Category


# Hangi uygulama altındaki html dosyasının çağırıldığını gösterir.

def index(request):
    context={
        "blogs":Blog.objects.filter(is_active=True,is_home=True),
        "categories":Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context={
        "blogs":Blog.objects.filter(is_active=True),
        "categories":Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def contact(request):
    context={
        "contact":Blog.objects.filter(is_active=True),
        "categories":Category.objects.all()

    }
    return render(request, "blog/contact.html", context)

def about(request):
    context={
        "about":Blog.objects.filter(is_active=True),
        "categories":Category.objects.all()
    }
    return render(request, "blog/about.html", context)

def blog_details(request, slug):
    blog=Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {
        "blog":blog
    })

def blogs_by_category(request, slug):
     context={
        "blogs":Blog.objects.filter(is_active=True, category__slug=slug),
        "categories":Category.objects.all(),
        "selected_category":slug
    }
     return render(request, "blog/blogs.html", context)



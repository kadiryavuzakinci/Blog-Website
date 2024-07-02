from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import ContactForm
# Create your views here.
def form_request(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            messages.success(request, 'Mesajınız Başarıyla Gönderildi!')
            return redirect("success")
    else:
        form = ContactForm()
    return render(request, "contacts/form.html", {'form': form})

def success(request):
    return render(request, "contacts/success.html")
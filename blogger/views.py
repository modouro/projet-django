from django.shortcuts import render, redirect
from django.contrib.auth.forms import AjouterBlog



def add_blog(request):
    if request.method == "POST":
        form = AjouterBlog(request.POST)
        if form.is_valid():
            form.save()
            # titre       = form.cleaned_data.get("titre")
            # description = form.cleaned_data.get("description")
            # contenu     = form.cleaned_data.get("contenu")
            return redirect('index')
    else:
         form = AjouterBlog()

    return (request, "/ajouter.html", {"form": form})

# Create your views here.

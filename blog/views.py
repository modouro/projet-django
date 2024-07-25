from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog


def home(request):
    message = "Bonjours mon cher"
    context = {'message': message}
    return render(request, "pages/index.html", context)

def mon_blog(request):
    blogs = Blog.objects.all()
    number = 10
    pagination = Paginator(blogs, number)  # pagination affichage par page de 10
    num_page = request.GET.get('page')
    try:
        blogs = pagination.page(num_page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        blogs = pagination.page(1)
    except EmptyPage:
        # Si la page est hors limites (par exemple, page 9999), afficher la dernière page
        blogs = pagination.page(pagination.num_pages)
    return render(request, "bloggers/mes_blog.html", {'blogs': blogs})

def about(request):
    message = "A propos de mon blog"
    blog = {'message': message}
    return render(request, "pages/about.html", blog)

def detail_article(request, id):
    blogs = get_object_or_404(Blog, id=id)
    return render (request, "bloggers/detail.html", {'blogs': blogs})

@login_required(login_url="login")
def new_article(request):
    if request.method == "POST":
        auteur      = request.user
        titre       = request.POST['titre']  
        description = request.POST['description']
        contenu     = request.POST['contenu']
        # print('auteur :', auteur)
        if titre and description and contenu:
            create_blog = Blog.objects.create(
                auteur      = auteur,
                titre       = titre,
                description = description,
                content     = contenu       #content de la data bases
            )
        create_blog.save()
        return redirect("/new_article/new/")     # ce n'est pas une urls dynamique
    return render (request, "bloggers/new_article.html")

@login_required(login_url="login")
def update_article(request, id):
    blogs = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        titre       = request.POST['titre']  
        description = request.POST['description']
        contenu     = request.POST['contenu']
        update_to_artcle = Blog.objects.filter(pk=blogs.id)
        update_to_artcle.update(
            titre       = titre,
            description = description,
            content     = contenu)      #content de la data bases
        return redirect("/blog/")
    return render (request, "bloggers/update_article.html", {'blogs': blogs})

@login_required(login_url="login")
def delete_article(request, id):
    blogs = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        blogs.delete()
        return redirect("/blog/")
    return render (request, "bloggers/delete_article.html", {"blogs": blogs} )

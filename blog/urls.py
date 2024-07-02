from django.urls import path
from .views import home, about, new_article, mon_blog,  detail_article, update_article, delete_article # .views montre qu'ils sont dans le même dossiers


urlpatterns = [
    path ("", home, name = "index"),
    path ("about/", about, name = "propos"),
    path ("blog/", mon_blog, name="blog"),
    path ("new_article/new/", new_article, name="ajouter"),
    path ("detail_article/<int:id>/", detail_article, name="detail"),
    path ("update_artcle/edit/<int:id>/", update_article, name="edit_artcle"),
    path ("delete_artcle/delete/<int:id>/", delete_article, name="delete_artcle"),
]



# Page not found (404)  Request Method:	GET  Request URL:	http://localhost:8000/about/
# si ok erreu TemplateDoesNotExist at /about/  sinon restez 


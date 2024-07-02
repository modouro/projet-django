from django.urls import path
from .views import add_blog


urlpatterns = [
    path ("ajouter/", add_blog, name="ajouter")
]

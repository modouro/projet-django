from django.contrib import admin
from .models import Blog    #import la base de données dans la page administrateur


admin.site.register(Blog)   # appel le model dans la base de données

# Register your models here.

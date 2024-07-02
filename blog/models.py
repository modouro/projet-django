from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User


class Blog(models.Model):
    titre       = models.CharField(max_length=100)
    description = models.TextField()
    content     = models.TextField()
    auteur      = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

# Create your models here.

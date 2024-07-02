from django.urls import path
from .views import Form_view, Logout_view, Form_Sign


urlpatterns = [
    path("login/", Form_view, name="login"),
    path("register/", Form_Sign, name="resgiter"),
    path("logout/", Logout_view, name="logout"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_home_page, name="home"),
    path("privacy/", views.view_privacy, name="privacy"),
]

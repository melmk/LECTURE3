from django.urls import URLPattern
from . import views

urlpatters = [
    path("", views.index, name=index)
]
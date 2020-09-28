from django.urls import path
from . import views


urlpatterns = [
    path('aboutAuthor', views.aboutme_view, name='aboutme')
]
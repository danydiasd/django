from django.urls import path
from . import views

# /blog/teste

urlpatterns = [
    path('teste/', views.teste)
]
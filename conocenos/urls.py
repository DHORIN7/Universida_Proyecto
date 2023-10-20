from django.urls import path 
from . import views

urlpatterns = [
    
    path('', views.conocenos, name="Conocenos"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria")
]
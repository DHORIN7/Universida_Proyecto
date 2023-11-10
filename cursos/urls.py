from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.cursos, name="Cursos"),
    path('exito', views.exito, name="Exito"),
    path('categoriacurso/<int:categoriacurso_id>/', views.categoriacurso, name="categoriacurso"),

]
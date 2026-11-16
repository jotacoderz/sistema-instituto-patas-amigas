from django.contrib import admin
from django.urls import path
from animais import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("animais/", views.lista_animais, name="lista_animais"),
    path("animais/novo/", views.cadastrar_animal, name="cadastrar_animal"),
]

from django.urls import path

from . import views


urlpatterns = [
    path('novo_pet/', views.novo_pet, name='novo_pet'),
    path('seus_pets/', views.seus_pets, name='seus_pets'),
    path('remover_pet/<slug:slug>/', views.remover_pet, name='remover_pet'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api_adocoes_por_raca/', views.api_adocoes_por_raca, name='api_adocoes_por_raca'),
]

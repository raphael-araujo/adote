from django.urls import path

from . import views


urlpatterns = [
    path('seus_pets/', views.seus_pets, name='seus_pets'),
    path('remover_pet/<slug:slug>/', views.remover_pet, name='remover_pet'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

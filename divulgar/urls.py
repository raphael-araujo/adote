from django.urls import path

from . import views


urlpatterns = [
    path('novo_pet/', views.novo_pet, name='novo_pet'),
    path('seus_pets/', views.seus_pets, name='seus_pets'),
    path('remover_pet/<slug:slug>/', views.remover_pet, name='remover_pet'),
    path('ver_pedidos_adocao/', views.ver_pedidos_adocao, name='ver_pedidos_adocao'),
    path('processar_pedido/<int:id>', views.processar_pedido, name='processar_pedido'),
]

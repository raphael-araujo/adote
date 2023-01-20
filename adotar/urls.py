from django.urls import path

from . import views


urlpatterns = [
    path('', views.listar_pets, name='listar_pets'),
    path('ver_pet/<slug:slug>', views.ver_pet, name='ver_pet'),
    path('pedido_adocao/<slug:slug>', views.pedido_adocao, name='pedido_adocao'),
    path('processar_pedido/<int:id>', views.processar_pedido, name='processar_pedido'),
]

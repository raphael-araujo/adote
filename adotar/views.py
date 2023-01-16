from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, redirect, render

from divulgar.models import Pet, Raca

from .models import PedidoAdocao


@login_required(login_url='login')
def listar_pets(request):
    pets = Pet.objects.filter(status='P')
    racas = Raca.objects.all()
    filtro_cidade = request.GET.get('cidade')
    filtro_raca = request.GET.get('raca')

    if filtro_cidade:
        pets = Pet.objects.filter(
            cidade__icontains=filtro_cidade).filter(status='P')
    if filtro_raca:
        pets = Pet.objects.filter(raca=filtro_raca).filter(status='P')
        filtro_raca = int(filtro_raca)

    context = {
        'pets': pets,
        'racas': racas,
        'filtro_raca': filtro_raca,
        'filtro_cidade': filtro_cidade
    }

    return render(request, 'listar_pets.html', context)


@login_required(login_url='login')
def ver_pet(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    context = {
        'pet': pet
    }

    return render(request, 'ver_pet.html', context)


@login_required(login_url='login')
def pedido_adocao(request, slug):
    pet = Pet.objects.filter(slug=slug).filter(status='P')

    try:
        if not pet.exists():
            messages.add_message(
                request,
                constants.ERROR,
                message='Esse pet já foi adotado.'
            )
            return redirect(to='listar_pets')

        adocao = PedidoAdocao(
            pet=pet.first(),
            usuario=request.user,
            data=datetime.now()
        )
        adocao.save()

        messages.add_message(
            request,
            constants.SUCCESS,
            message='Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.'
        )
        return redirect(to='listar_pets')

    except:
        messages.add_message(
            request,
            constants.ERROR,
            message='Erro interno do sistema.'
        )
        return redirect(to='listar_pets')

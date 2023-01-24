from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from divulgar.models import Pet, Raca

from .models import PedidoAdocao


@login_required(login_url='login')
def listar_pets(request):
    pets = Pet.objects.filter(status='P').exclude(usuario=request.user)
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


@login_required(login_url='login')
def processar_pedido(request, id):
    status = request.GET.get('status')
    pedido = get_object_or_404(PedidoAdocao, id=id)
    pet = get_object_or_404(Pet, id=pedido.pet.id)

    try:
        if status == 'A':
            pedido.status = 'AP'
            pet.status = 'A'
            pet.save()
            mensagem = f"""Olá {pedido.usuario.username}, seu pedido de adoção foi aprovado com sucesso!"""
        elif status == 'R':
            pedido.status = 'R'
            mensagem = f"""Olá {pedido.usuario.username}, infelizmente não podemos dar prosseguimento 
                        com a adoção, sentimos muito."""
        else:
            messages.add_message(
                request,
                constants.ERROR,
                message='Erro ao concluir operação.'
            )
            return redirect(to='ver_pedidos_adocao')

        pedido.save()

        send_mail(
            subject='Sua adoção foi processada',
            message=mensagem,
            from_email='teste@email.com.br',
            recipient_list=[pedido.usuario.email,]
        )
        messages.add_message(
            request,
            constants.SUCCESS,
            message='Pedido de adoção processado com sucesso.'
        )
        return redirect(to='ver_pedidos_adocao')

    except:
        messages.add_message(
            request,
            constants.ERROR,
            message='Erro interno do sistema.'
        )
        return redirect(to='ver_pedidos_adocao')


@login_required(login_url='login')
def ver_pedidos_adocao(request):
    pedidos = PedidoAdocao.objects.filter(
        pet__usuario=request.user).filter(status='AG')

    context = {
        'pedidos': pedidos
    }

    return render(request, 'ver_pedidos_adocao.html', context)

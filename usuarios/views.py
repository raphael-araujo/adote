from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .utils import cadastro_is_valid

# Create your views here.


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if not cadastro_is_valid(request, nome, email, senha, confirmar_senha):
            return redirect(to='cadastro')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            messages.add_message(
                request,
                constants.SUCCESS,
                message='Usuário cadastrado com sucesso.'
            )
            return redirect(to='login')

        except:
            messages.add_message(
                request,
                constants.WARNING,
                message='Este usuário já existe.'
            )
            return redirect(to='cadastro')

    else:
        return render(request, 'cadastro.html')

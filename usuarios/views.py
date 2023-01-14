from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
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

        user = User.objects.filter(username=nome)
        user_email = User.objects.filter(email=email)

        if user.exists():
            messages.add_message(
                request,
                constants.WARNING,
                message='Este usuário já existe.'
            )
            return redirect(to='cadastro')

        if user_email.exists():
            messages.add_message(
                request,
                constants.WARNING,
                message='Este email já está cadastrado.'
            )
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
                constants.ERROR,
                message='Erro interno do sistema.'
            )
            return redirect(to='cadastro')

    else:
        if request.user.is_authenticated:
            return redirect(to='/divulgar/novo_pet')

        return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        senha = request.POST['senha']
        user = auth.authenticate(username=nome, password=senha)

        if not user:
            messages.add_message(
                request,
                constants.ERROR,
                message='Usuário ou senha inválidos'
            )
            return redirect(to='login')
        else:
            auth.login(request, user)
            return redirect(to='seus_pets')

    else:
        if request.user.is_authenticated:
            return redirect(to='/divulgar/novo_pet')

        return render(request, 'login.html')


def sair(request):
    auth.logout(request)
    return redirect(to='login')

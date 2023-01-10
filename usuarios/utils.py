from django.contrib import messages
from django.contrib.messages import constants


def cadastro_is_valid(request, nome, email, senha, confirmar_senha):
    if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
        messages.add_message(
            request,
            constants.ERROR,
            message='Preencha todos os campos.'
        )
        return False

    if senha != confirmar_senha:
        messages.add_message(
            request,
            constants.ERROR,
            message='As senhas não coincidem.'
        )
        return False

    return True

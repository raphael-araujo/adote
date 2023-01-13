from django.contrib import messages
from django.contrib.messages import constants


def pet_is_valid(request, foto, nome, descricao, estado, cidade, telefone, tags, raca):
    if (not foto) or (len(nome.strip()) == 0) or (len(descricao.strip()) == 0) or (len(estado.strip()) == 0) or (len(cidade.strip()) == 0) or (len(telefone.strip()) == 0) or (len(tags) == 0) or (len(raca.strip()) == 0):
        messages.add_message(
            request,
            constants.ERROR,
            message='Preencha todos os campos.'
        )

        return False

    if foto.size > 100_000_000:
        messages.add_message(
            request,
            constants.ERROR,
            message='A foto do pet deve ter menos de 10MB.'
        )

        return False

    return True

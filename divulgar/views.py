from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import redirect, render

from .models import Pet, Raca, Tag
from .utils import pet_is_valid

# Create your views here.


@login_required(login_url='login')
def novo_pet(request):
    if request.method == 'POST':
        foto = request.FILES.get('foto')
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        estado = request.POST['estado']
        cidade = request.POST['cidade']
        telefone = request.POST['telefone']
        tags = request.POST.getlist('tags')
        raca = request.POST['raca']

        if not pet_is_valid(request, foto, nome, descricao, estado, cidade, telefone, tags, raca):
            return redirect(to='novo_pet')

        try:
            p = Pet(
                usuario=request.user,
                foto=foto,
                nome=nome,
                descricao=descricao,
                estado=estado,
                cidade=cidade,
                telefone=telefone,
                raca_id=raca,
            )
            p.save()
            p.tags.add(*tags)
            p.slug = f'{nome}-{p.id}'
            p.save()

            messages.add_message(
                request,
                constants.SUCCESS,
                message=f'O pet "{nome}" foi cadastrado com sucesso.'
            )
            return redirect(to='novo_pet')

        except:
            messages.add_message(
                request,
                constants.ERROR,
                message='Erro interno do sistema.'
            )
            return redirect(to='novo_pet')

    else:
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        context = {
            'tags': tags,
            'racas': racas
        }

        return render(request, 'novo_pet.html', context)

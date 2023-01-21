from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt

from adotar.models import PedidoAdocao

from .models import Pet, Raca, Tag
from .utils import pet_is_valid

# Create your views here.


@login_required(login_url='login')
def seus_pets(request):
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
            p.slug = slugify(f'{nome} {p.id}')
            p.save()

            messages.add_message(
                request,
                constants.SUCCESS,
                message=f'O pet "{nome}" foi cadastrado com sucesso.'
            )
            return redirect(to='seus_pets')

        except:
            messages.add_message(
                request,
                constants.ERROR,
                message='Erro interno do sistema.'
            )
            return redirect(to='novo_pet')
        
    else:
        pets = Pet.objects.filter(usuario=request.user)
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        context = {
            'pets': pets,
            'tags': tags,
            'racas': racas
        }

        return render(request, 'seus_pets.html', context)


@login_required(login_url='login')
def remover_pet(request, slug):
    pet = Pet.objects.filter(usuario=request.user).filter(slug=slug)

    if pet:
        pet.delete()

        messages.add_message(
            request,
            constants.WARNING,
            message=f'Pet removido com sucesso.'
        )
        return redirect(to='seus_pets')
    else:
        messages.add_message(
            request,
            constants.ERROR,
            message=f'Erro ao realizar a operação.'
        )
        return redirect(to='seus_pets')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


@csrf_exempt
def api_adocoes_por_raca(request):
    racas = Raca.objects.all()

    quantidade_adocoes = []
    for raca in racas:
        adocoes = PedidoAdocao.objects.filter(pet__raca=raca).count()
        quantidade_adocoes.append(adocoes)

    racas = [raca.raca for raca in racas]
    data = {
        'quantidade_adocoes': quantidade_adocoes,
        'labels': racas
    }
    return JsonResponse(data)

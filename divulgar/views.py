from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
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
            return redirect(to='seus_pets')

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
            return redirect(to='seus_pets')

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
            message=f'Erro ao realizar a opera????o.'
        )
        return redirect(to='seus_pets')


@login_required(login_url='login')
@csrf_exempt
def dashboard(request):
    filtro_estado = request.GET.get('estado')
    racas = [raca.raca for raca in Raca.objects.all().order_by('raca')]

    estados = []
    for pet in Pet.objects.all():
        if not pet.estado in estados:
            estados.append(pet.estado)

    quantidade_adocoes = []
    for raca in racas:
        if filtro_estado:
            pedidos_por_estado = PedidoAdocao.objects.filter(
                pet__estado=filtro_estado).filter(pet__raca__raca=raca).filter(status='AP').count()
            quantidade_adocoes.append(pedidos_por_estado)
        else:
            adocoes = PedidoAdocao.objects.filter(
                pet__raca__raca=raca).filter(status='AP').count()
            quantidade_adocoes.append(adocoes)

    context = {
        'quantidade_adocoes': quantidade_adocoes,
        'total_quantidade_adocoes': sum(quantidade_adocoes),
        'labels': racas,
        'estados': sorted(estados),
        'filtro_estado': filtro_estado
    }

    return render(request, 'dashboard.html', context)

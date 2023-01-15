from django.shortcuts import render

from divulgar.models import Pet, Raca

# Create your views here.


def listar_pets(request):
    pets = Pet.objects.filter(status='P')
    racas = Raca.objects.all()
    filtro_cidade = request.GET.get('cidade')
    filtro_raca = request.GET.get('raca')

    if filtro_cidade:
        pets = Pet.objects.filter(cidade__icontains=filtro_cidade).filter(status='P')
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

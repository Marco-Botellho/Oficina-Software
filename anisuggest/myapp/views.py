from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Animes, Profile, Rating
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

def index(request):
    return render(request, 'usuarios/index.html')

def cadastro(request):
    if request.method == "POST":
        POST = request.POST
        email = POST.get("email")
        first_name = POST.get("first_name")
        last_name = POST.get("last_name")
        password = POST.get("password")
        confirm_password = POST.get("password2")
        if password == confirm_password:
            # Verificar se o email já está em uso
            if not User.objects.filter(username=email).exists():
                # Criar o usuário
                user = User.objects.create_user(email=email, username=email, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                # Criar o perfil associado ao usuário e atribuir o nome
                profile, created = Profile.objects.get_or_create(user=user)
                profile.nome = first_name
                profile.save()

                return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile_url = reverse('user_profile', kwargs={'id': user.profile.id}) if user.profile else None
            print(f"Profile URL: {profile_url}")
            return redirect('user_profile', id=user.profile.id)
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

"""
@login_required
def logado(request):
    animes = Animes.objects.all()
    context = {
        'animes': animes
    }
    return render(request, 'usuarios/logado.html', context)


@login_required
def user_profile(request, id):
    #user_profile = User.objects.filter(id=id).first()
    profile = Profile.objects.filter(id=id).first()
    context = {
        'profile':profile
    }
    return render(request, 'usuarios/logado.html', context)"""

@login_required
def user_profile(request, id=None):
    if id is not None:
        profile = Profile.objects.filter(id=id).first()
        animes = Animes.objects.all()
        context = {
            'profile': profile,
            'animes': animes
        }
        return render(request, 'usuarios/user_profile.html', context)
    else:
        # Lidar com o caso em que id não está presente
        return HttpResponse("ID não fornecido")
    
@login_required
def filtro(request):
    profile = request.user.profile
    id = profile.id

    filtro_anime = request.GET.get('anime', None)
    data_query = {}

    if filtro_anime:
        data_query['name__icontains'] = filtro_anime

    filtragem = Animes.objects.filter(**data_query).order_by('name', 'id')
    
    if filtragem.exists():
        # Filtrar apenas valores únicos na coluna "name"
        unique_names = set()
        unique_results = []
        
        for anime in filtragem:
            if anime.name not in unique_names:
                unique_names.add(anime.name)
                unique_results.append(anime)
        
        context = {
            'id': id,
            'filtragem': unique_results
        }

    else:
        # Se não houver resultados, definir a variável filtragem como None
        context = {
            'id': id,
            'filtragem': None
        }
    return render(request, 'usuarios/filtro.html', context)

@login_required
def avaliar_anime(request):
    id = request.user.id  # Use isso se o ID do usuário estiver disponível no request.user.id
    
    if request.method == "POST":
        anime_id = request.POST.get("anime_id", None)
        valor = int(request.POST.get("valor", 0))
        descricao = request.POST.get("descricao", "")

        # Certifique-se de que o ID do anime e do usuário está disponível antes de continuar
        if anime_id is not None and id is not None:
            profile = Profile.objects.get(id=id)
            anime = Animes.objects.get(id=anime_id)

            # Verifica se já existe uma avaliação para este usuário e anime
            nota, created = Rating.objects.get_or_create(user_id=profile, anime_id=anime)
            
            nota.rating = valor
            nota.descricao = descricao
            nota.save()

            return redirect('user_profile', id=id)
    
    # Se o método não for POST, renderiza a página com o formulário de avaliação
    context = {
        'id': id,
    }
    return render(request, 'usuarios/filtro.html', context)
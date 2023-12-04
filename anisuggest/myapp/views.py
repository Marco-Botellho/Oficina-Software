from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Animes, Profile, Rating
from django.urls import reverse
from .forms import RatingForm

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
            'filtragem': unique_results,
            'rating_form': RatingForm(),
        }

    else:
        # Se não houver resultados, definir a variável filtragem como None
        context = {
            'id': id,
            'filtragem': None,
            'rating_form': RatingForm(),
        }
    return render(request, 'usuarios/filtro.html', context)

    
@login_required
def avaliar_anime(request):
    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        
        try:
            if rating_form.is_valid():
                anime_id = POST.get("anime")
                profile_id = POST.get("profile")
                valor = POST.get('rating')

                profile1 = get_object_or_404(Profile, id=profile_id)
                anime1 = get_object_or_404(Animes, id=anime_id)

                #rating, created = Rating.objects.get_or_create(user=profile1, anime=anime1, defaults={'rating': valor})
                rating = Rating.objects.aget_or_create(user=profile1, anime=anime1, rating=valor)
                
                #if not created:
                #rating.rating = valor
                rating.save()
                    
                return HttpResponse("Avaliação realizada com sucesso!")
            
        except Profile.DoesNotExist:
            return HttpResponse("Perfil não encontrado.")
        
        except Animes.DoesNotExist:
            return HttpResponse("Anime não encontrado.")

        return HttpResponse("Formulário inválido. Avaliação não realizada.")
    else:
        return HttpResponse("Método não permitido para avaliação de anime.")
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

                # Verificar se o usuário já possui um perfil
                if not hasattr(user, 'profile'):
                    # Criar o perfil associado ao usuário
                    profile = Profile.objects.create(user=user, nome=first_name)

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
    

def filtro(request):
  mydata = Animes.objects.filter(name__icontains='one punch').order_by('name', 'id').values()
  template = loader.get_template('usuarios/filtro.html')
  context = {
    'filtragem': mydata
  }
  return HttpResponse(template.render(context, request))
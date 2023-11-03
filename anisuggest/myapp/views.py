from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Animes
from .models import Rating
from django.contrib.auth.decorators import login_required


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
            user = User.objects.create_user(email=email, username=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('logado', id=user.user_profile.id)
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('usuarios/index.html')


@login_required
def logado(request, id):
    user_profile = User.objects.filter(id=id).first()
    
    return render(request, 'logado.html', context)
    

@login_required
def logado(request):

    animes = Animes.objects.all()
    context = {
        'animes': animes
    }

    return render(request, 'usuarios/logado.html', context)
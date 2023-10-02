from django.shortcuts import render #HttpResponse


def index(request):
    return render(request, 'usuarios/index.html')

    #return HttpResponse("Hello, World!")

def login(request):
    return render(request, 'usuarios/login.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')


# def home(request):
    # return render(request, 'usuarios/home.html')

"""
# from .models import Usuario

def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.sobrenome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    # Retornar os dados para a página de listagem de usuários
    return render(request,'usuarios/usuarios.html',usuarios)"""
from django.urls import path
from . import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('',views.index,name="index"),
    # path('',views.home,name="home"),

    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios'),

    # usuarios.com/login
    path('login/',views.login,name='login'),

    # usuarios.com/cadastro
    path('cadastro/',views.cadastro,name='cadastro'),

]

from django.urls import path
from . import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('',views.index,name="index"),

    # usuarios.com/login
    path('login/',views.login,name='login'),

    # usuarios.com/login
    path('', views.logout_view, name= 'logout'),

    # usuarios.com/cadastro
    path('cadastro/',views.cadastro,name='cadastro'),

    # usuarios.com/logado
    path('logado/',views.logado,name='logado'),

]

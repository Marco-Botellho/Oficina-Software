from django.urls import path
from . import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('',views.index,name="index"),

    # usuarios.com/login
    path('login/',views.user_login,name='login'),

    # usuarios.com/login
    path('index', views.logout_view, name= 'logout'),

    # usuarios.com/cadastro
    path('cadastro/',views.cadastro,name='cadastro'),

    # usuarios.com/user_profile
    path('user_profile/<int:id>/',views.user_profile,name='user_profile'),

    # usuarios.com/filtro
    path('filtro/',views.filtro,name='filtro'),

]

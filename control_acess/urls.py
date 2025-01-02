from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('atualiza_cidades/', views.attcidade, name='attcidade'),
    # path('register/', views.register, name='register'),
]
# Compare this snippet from control_acess/views.py:

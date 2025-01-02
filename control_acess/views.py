from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from django.contrib.auth.models import User
from .models import cidade
# Create your views here.


def index(request):
            # return render(request, 'index.html')
            
    return render(request, 'index.html', context={'title': 'Página Inicial', 'message': 'Olá, mundo!'})

def login(request):
    return HttpResponse('Login')

def attcidade(request):
    API_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/51/municipios"  # Substitua pela URL correta da sua API

    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        cidades = response.json()

        for cidade_data in cidades:
            codigo_ibge = cidade_data.get("id")
            nome = cidade_data.get("nome")
            estado_sigla = cidade_data["microrregiao"]["mesorregiao"]["UF"]["sigla"]

            # Verifique os valores antes de salvar
            if not all([codigo_ibge, nome, estado_sigla]):
                continue  # Pule entradas inválidas

            cidade.objects.update_or_create(
                codigo_ibge=codigo_ibge,
                defaults={
                    "nome": nome,
                    "estado": estado_sigla,
                    "pais": "Brasil"
                }
            )

        return JsonResponse({"status": "Cidades atualizadas com sucesso!"})
    except requests.RequestException as e:
        return JsonResponse({"error": f"Erro ao acessar a API: {e}"}, status=500)
    except KeyError as e:
        return JsonResponse({"error": f"Erro ao processar os dados: Chave {e} não encontrada"}, status=500)
    except Exception as e:
        return JsonResponse({"error": f"Erro desconhecido: {e}"}, status=500)
    return HttpResponse('Att Cidade')
import requests
from control_acess.models import cidade  # Substitua "myapp" pelo nome do seu app Django

# URL da API
API_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/50/municipios"  # Substitua pela URL correta da sua API

# Função para consumir a API e salvar os dados no banco de dados
def atualizar_cidades():
    try:
        # Fazendo a requisição para a API
        response = requests.get(API_URL)
        response.raise_for_status()  # Verifica se ocorreu algum erro na requisição
        
        # Processando o JSON retornado
        cidades = response.json()
        
        for cidade in cidades:
            # Extraindo as informações necessárias
            codigo_ibge = cidade.get("id")
            nome = cidade.get("nome")
            estado_sigla = cidade["microrregiao"]["mesorregiao"]["UF"]["sigla"]
            
            # Salvando no banco de dados
            cidade.objects.update_or_create(
                codigo_ibge=codigo_ibge,  # Campo usado para identificar se a cidade já existe
                defaults={
                    "nome": nome,
                    "estado": estado_sigla,
                    "pais": "Brasil"  # Ajuste se precisar de outra lógica para definir o país
                }
            )
        print("Cidades atualizadas com sucesso!")
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
    except KeyError as e:
        print(f"Erro ao processar os dados: Chave {e} não encontrada no retorno da API.")

# Chame a função no momento apropriado no seu código
if __name__ == "__main__":
    atualizar_cidades()

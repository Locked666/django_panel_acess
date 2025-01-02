from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# table buit in de cidades 
class cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    codigo_ibge = models.CharField(max_length=7)
    pais = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

# Tabela de entidades principais.
class entidade(models.Model):
    choice = (
        ('P', 'Prefeitura'),
        ('C', 'Câmara'),
        ('RPPS', 'RPPS'),
        ('SAAE', 'SAAE'),
        ('O', 'Outros'),
    )
    
    nome = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    tipo = models.CharField(max_length=4, choices=choice)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    cidade = models.OneToOneField(cidade, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome    


class config_acesso(models.Model):
    tp_conexao_choice = (
        (1, 'TeamViewer'),
        (2, 'AnyDesk'),
        (3, 'QSConect'),
    )
    status = models.BooleanField(default=True)
    entidade = models.OneToOneField(entidade, on_delete=models.CASCADE)
    tp_conexao = models.IntegerField(choices=tp_conexao_choice)
    id_conexao = models.CharField(max_length=100)
    senha_conexao = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)    
    senha_conexao = models.CharField(max_length=200)  # Aumente o tamanho para suportar o hash
    data_criacao = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        """Armazena a senha como um hash."""
        self.senha_conexao = make_password(raw_password)

    def check_password(self, raw_password):
        """Verifica se a senha fornecida corresponde ao hash armazenado."""
        return check_password(raw_password, self.senha_conexao)

class log_acesso(models.Model):
    entidade = models.ForeignKey(entidade, on_delete=models.CASCADE)
    tp_conexao = models.CharField(max_length=100)
    data_acesso = models.DateTimeField(auto_now=True)
    ip_acesso = models.GenericIPAddressField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.entidade.nome
from django.contrib import admin
from django import forms
from .models import entidade,config_acesso
# Register your models here.

# admin.site.register(entidade)
# admin.site.register(config_acesso)

class ConfigAcessoForm(forms.ModelForm):
    senha_conexao = forms.CharField(
        widget=forms.PasswordInput,
        required=False,  # Deixe opcional ao editar
        label="Senha de Conexão",
    )

    class Meta:
        model = config_acesso
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        senha = self.cleaned_data.get('senha_conexao')

        if senha:  # Atualiza apenas se uma nova senha for informada
            instance.set_password(senha)

        if commit:
            instance.save()
        return instance

class ConfigAcessoAdmin(admin.ModelAdmin):
    form = ConfigAcessoForm
    list_display = ('entidade', 'tp_conexao', 'status', 'data_criacao')
    list_filter = ('status', 'tp_conexao')
    search_fields = ('entidade__nome',)


class EntidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status', 'tipo', 'cnpj', 'email', 'telefone', 'endereco', 'cidade', 'cep', 'data_criacao')
    search_fields = ('nome', 'cnpj', 'email', 'telefone', 'endereco', 'cidade__nome', 'cep')
    list_filter = ('status', 'tipo', )
    
admin.site.register(config_acesso, ConfigAcessoAdmin)
admin.site.register(entidade,EntidadeAdmin)
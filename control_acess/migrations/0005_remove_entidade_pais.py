# Generated by Django 5.1.4 on 2025-01-02 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_acess', '0004_remove_entidade_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entidade',
            name='pais',
        ),
    ]

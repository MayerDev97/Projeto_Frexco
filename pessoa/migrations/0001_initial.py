# Generated by Django 4.1.3 on 2022-11-15 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('ativa', models.BooleanField(default=True)),
                ('senha', models.CharField(max_length=15, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
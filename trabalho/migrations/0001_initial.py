# Generated by Django 2.1.7 on 2019-05-17 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, help_text='Espaço para colocar qualquer informação.', null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Digite seu nome completo', max_length=100)),
                ('nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('email', models.EmailField(help_text='Digite seu e-mail', max_length=100)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trabalho.Cidade')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trabalho.Estado'),
        ),
    ]
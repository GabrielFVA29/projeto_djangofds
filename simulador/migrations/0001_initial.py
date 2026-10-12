import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Cenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('setor', models.CharField(max_length=60)),
                ('titulo', models.CharField(max_length=120)),
                ('problema', models.TextField()),
                ('perda_atual', models.PositiveIntegerField(help_text='Prejuízo atual em R$ por mês')),
                ('conceito_titulo', models.CharField(max_length=120)),
                ('conceito_resumo', models.TextField()),
                ('conceito_passos', models.TextField(help_text='Um passo por linha')),
                ('conceito_economia', models.TextField()),
            ],
            options={
                'verbose_name': 'cenário',
                'verbose_name_plural': 'cenários',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Rodada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogador', models.CharField(max_length=80)),
                ('empresa', models.CharField(max_length=80)),
                ('iniciada_em', models.DateTimeField(auto_now_add=True)),
                ('finalizada_em', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-iniciada_em'],
            },
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letra', models.CharField(max_length=1)),
                ('texto', models.CharField(max_length=200)),
                ('custo', models.PositiveIntegerField(help_text='Custo da solução em R$ por mês')),
                ('perda_restante', models.PositiveIntegerField(help_text='Prejuízo que continua em R$ por mês')),
                ('usa_iot', models.BooleanField(default=False)),
                ('explicacao', models.TextField()),
                ('cenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opcoes', to='simulador.cenario')),
            ],
            options={
                'verbose_name': 'opção',
                'verbose_name_plural': 'opções',
                'ordering': ['letra'],
                'unique_together': {('cenario', 'letra')},
            },
        ),
        migrations.CreateModel(
            name='Voz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('papel', models.CharField(max_length=60)),
                ('fala', models.TextField()),
                ('ordem', models.PositiveIntegerField(default=0)),
                ('cenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vozes', to='simulador.cenario')),
            ],
            options={
                'verbose_name': 'voz da equipe',
                'verbose_name_plural': 'vozes da equipe',
                'ordering': ['ordem'],
            },
        ),
        migrations.CreateModel(
            name='Decisao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decidida_em', models.DateTimeField(auto_now=True)),
                ('cenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulador.cenario')),
                ('opcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulador.opcao')),
                ('rodada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decisoes', to='simulador.rodada')),
            ],
            options={
                'verbose_name': 'decisão',
                'verbose_name_plural': 'decisões',
                'ordering': ['cenario__numero'],
                'unique_together': {('rodada', 'cenario')},
            },
        ),
    ]

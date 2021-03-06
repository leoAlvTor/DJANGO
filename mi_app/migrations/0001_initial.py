# Generated by Django 3.1.3 on 2020-11-27 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(verbose_name='TEST')),
                ('estado', models.TextField(default='DEFAULT')),
                ('descripcion', models.TextField(default='DEFAULT VALUE')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grupo', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mi_app.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Red_Social',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(default='NA')),
                ('url', models.TextField(default='NA')),
                ('estado', models.TextField(default='NA')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('email_recuperacion', models.TextField()),
                ('password', models.TextField()),
                ('numero', models.TextField()),
                ('ubicacion', models.TextField()),
                ('estado', models.TextField()),
                ('ciudad', models.TextField()),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('fecha_nacimiento', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(default='NA')),
                ('token_parteA', models.TextField(default='NA')),
                ('token_parteB', models.TextField(default='NA')),
                ('red_social', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mi_app.red_social')),
                ('usuario', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mi_app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(default='TESTING MESSAGE')),
                ('hashtag', models.TextField(default='#TEST')),
                ('link', models.TextField(default='https://www.google.com')),
                ('ubicacion', models.TextField(default='NA')),
                ('hora_envio', models.DateTimeField(null=True)),
                ('estado', models.CharField(default='E', max_length=1)),
                ('grupo', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mi_app.grupo_usuario')),
                ('red_social', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mi_app.red_social')),
                ('usuario', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mi_app.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='grupo_usuario',
            name='usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mi_app.usuario'),
        ),
    ]

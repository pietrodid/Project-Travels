# Generated by Django 3.1.2 on 2020-11-06 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=10)),
                ('capacidad_maxima', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=30)),
                ('comuna', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('identidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trayecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('precio', models.FloatField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.bus')),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Trayecto_destino', to='restapi.terminal')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Trayecto_origen', to='restapi.terminal')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='chofer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.usuario'),
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trayecto', models.IntegerField()),
                ('fecha_de_compra', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restapi.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('boleto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restapi.boleto')),
            ],
        ),
    ]
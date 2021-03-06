# Generated by Django 3.1.7 on 2021-04-15 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_auto_20210403_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion_cliente', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inversion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tabla', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre_tipo', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion_tipo', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion_proyecto', models.CharField(blank=True, max_length=200, null=True)),
                ('financiamiento_proyecto', models.CharField(blank=True, max_length=45, null=True)),
                ('photo', models.CharField(blank=True, max_length=500, null=True)),
                ('acumulado', models.IntegerField(blank=True, null=True)),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='core.cliente')),
                ('id_inversion', models.ForeignKey(blank=True, db_column='id_inversion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.inversion')),
            ],
        ),
        migrations.CreateModel(
            name='Inversionista',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo_inversionista', models.CharField(blank=True, max_length=45, null=True)),
                ('empresa_inversionista', models.CharField(blank=True, max_length=45, null=True)),
                ('id_tipo', models.ForeignKey(blank=True, db_column='id_tipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipo')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='inversion',
            name='id_tipo',
            field=models.ForeignKey(blank=True, db_column='id_tipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipo'),
        ),
        migrations.CreateModel(
            name='Experto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo_experto', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion_experto', models.CharField(blank=True, max_length=200, null=True)),
                ('id_tipo', models.ForeignKey(blank=True, db_column='id_tipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipo')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_tipo',
            field=models.ForeignKey(blank=True, db_column='id_tipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario'),
        ),
    ]

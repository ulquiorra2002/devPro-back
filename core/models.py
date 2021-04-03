from django.db import models

class Tipo(models.Model):
    nombre_tabla = models.CharField(max_length=45, blank=True, null=True)
    nombre_tipo = models.CharField(max_length=45, blank=True, null=True)
    descripcion_tipo = models.CharField(max_length=45, blank=True, null=True)

class Experto(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE)
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')
    codigo_experto = models.CharField(max_length=45, blank=True, null=True)
    descripcion_experto = models.CharField(max_length=200, blank=True, null=True)

class Inversion(models.Model):
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')

class Inversionista(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE)
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')
    codigo_inversionista = models.CharField(max_length=45, blank=True, null=True)
    empresa_inversionista = models.CharField(max_length=45, blank=True, null=True)


class Etapa(models.Model):
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')

class Proyecto(models.Model):
    id_etapa = models.ForeignKey(Etapa, models.DO_NOTHING, db_column='id_etapa')
    id_inversion = models.ForeignKey(Inversion, models.DO_NOTHING, db_column='id_inversion')
    nombre_proyecto = models.CharField(max_length=45, blank=True, null=True)
    descripcion_proyecto = models.CharField(max_length=200, blank=True, null=True)
    financiamiento_proyecto = models.CharField(max_length=45, blank=True, null=True)

class Cliente(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE)
    id_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='id_proyecto')
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')
    descripcion_cliente = models.CharField(max_length=45, blank=True, null=True)

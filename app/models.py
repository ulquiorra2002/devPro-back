from django.db import models

class Persona(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    numero_documento_persona = models.CharField(max_length=45, blank=True, null=True)
    direccion_persona = models.CharField(max_length=45, blank=True, null=True)
    usuario= models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'persona'

class Tipo(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nombre_tabla = models.CharField(max_length=45, blank=True, null=True)
    nombre_tipo = models.CharField(max_length=45, blank=True, null=True)
    descripcion_tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo'

class Experto(models.Model):
    id_experto = models.IntegerField(primary_key=True)
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')
    codigo_experto = models.CharField(max_length=45, blank=True, null=True)
    descripcion_experto = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experto'
        unique_together = (('id_experto', 'id_persona', 'id_tipo'),)


class Inversion(models.Model):
    id_inversion = models.IntegerField(primary_key=True)
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'inversion'
        unique_together = (('id_inversion', 'id_tipo'),)


class Inversionista(models.Model):
    id_inversionista = models.IntegerField(primary_key=True)
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')
    codigo_inversionista = models.CharField(max_length=45, blank=True, null=True)
    empresa_inversionista = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inversionista'
        unique_together = (('id_inversionista', 'id_persona', 'id_tipo'),)



class Etapa(models.Model):
    id_etapa =  models.IntegerField(primary_key=True)
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'etapa'
        unique_together = (('id_etapa', 'id_tipo'),)

class Proyecto(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    id_etapa = models.ForeignKey(Etapa, models.DO_NOTHING, db_column='id_etapa')
    id_inversion = models.ForeignKey(Inversion, models.DO_NOTHING, db_column='id_inversion')
    nombre_proyecto = models.CharField(max_length=45, blank=True, null=True)
    descripcion_proyecto = models.CharField(max_length=200, blank=True, null=True)
    financiamiento_proyecto = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto'
        unique_together = (('id_proyecto', 'id_etapa', 'id_inversion'),)






class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    id_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='id_proyecto')
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')
    descripcion_cliente = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
        unique_together = (('id_cliente', 'id_persona', 'id_proyecto', 'id_tipo'),)

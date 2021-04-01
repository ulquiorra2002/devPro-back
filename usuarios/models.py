from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    email = models.EmailField(unique=True, error_messages={
                              'unique': "ya existe este correo"})
    photo = models.CharField(max_length=500,null=True,blank=True)
    tipo_usuario = models.CharField(max_length=50,null=True,blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):

        return self.username
from django.db import models

class Staff(models.Model):
    id_staff = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)
    controle_hora = models.DurationField()

    def __str__(self):
        return self.login

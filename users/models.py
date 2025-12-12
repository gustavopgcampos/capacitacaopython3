from django.db import models

# modelo padrão do usuário no banco de dados
class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.nome
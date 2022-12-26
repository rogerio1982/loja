

from django.db import models
# teste github 4

class produto(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class cliente(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class vendas(models.Model):
    role_name = models.CharField(max_length=100)
    produto = models.ForeignKey('produto', on_delete=models.CASCADE, related_name='produto')
    cliente = models.ForeignKey('cliente', on_delete=models.CASCADE, related_name='cliente')
    def __str__(self):
        return self.role_name

from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=120,null=False,blank=False,unique=True)

    def __str__(self):
        return self.categoria

class Marca(models.Model):
    marca = models.CharField(max_length=120,null=False,blank=False,unique=True)

    def __str__(self):
        return self.marca

class Produto(models.Model):
    referencia = models.CharField(max_length=120,null=False,blank=False,unique=True)
    name = models.CharField(max_length=120,null=False,blank=False)
    marca = models.ForeignKey(Marca,on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(null=False,blank=False)
    aplicacao = models.CharField(max_length=600,null=False,blank=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    preço_venda = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10000)])
    preço_compra = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10000)])

    def __str__(self):
        return self.referencia
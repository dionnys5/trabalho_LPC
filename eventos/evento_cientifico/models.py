from django.db import models
from django.contrib.auth.models import User



class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=258)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11)
    
    class Meta:
        verbose_name = 'Pessoa Fisica'
        verbose_name_plural = 'Pessoas Fisicas'

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=14)
    razaoSocial = models.CharField(max_length=150, null=True)
    
    class Meta:
        verbose_name = 'Pessoa Juridica'
        verbose_name_plural = 'Pessoas Juridica'

class Autor(Pessoa):
    curriculo = models.CharField(max_length=128)   
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    eventoPrincipal = models.CharField(max_length=128)
    nome = models.CharField(max_length=128)
    data_inicio = models.DateTimeField()
    palavrasChave = models.CharField(max_length=128)
    logotipo = models.CharField(max_length=128)
    palavrasChave = models.CharField(max_length=128)
    realizador = models.ForeignKey(Pessoa, related_name='realizadores', null=True, blank=False)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    endereco = models.CharField(max_length=250)
    cep = models.CharField(max_length=8)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    
    def __str__(self):
        return self.nome

class EventoCientifico(Evento):
    issn = models.CharField(max_length=9)

    class Meta:
        verbose_name = 'Evento Cientifico'
        verbose_name_plural = 'Eventos Cientificos'


class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=128)
    evento = models.ForeignKey(EventoCientifico, related_name='evento', null=True, blank=False)
    class Meta:
        verbose_name = 'Artigo Cientifico'
        verbose_name_plural = 'Artigos Cientificos'



class Publicacao(models.Model):
    autor = models.ForeignKey(Autor, related_name='Autor', null=True, blank=False)
    artigo = models.ForeignKey(ArtigoCientifico, related_name='ArtigoCientifico', null=True, blank=False)
    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
        
    def __str__(self):
        return "Autor: " + self.autor.nome +" Artigo: "+ self.artigo.titulo

    

from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(
        max_length=100
    )
    descricao = models.CharField(
        max_length=100
    )
    publico = models.TextField(
        null=True,
    )
    slug = models.SlugField(
        max_length=255,
        null=True,
        unique=True
    )

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse_lazy(
            'modulos:detalhe', kwargs={'slug': self.slug}
        )

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)


class Aula(OrderedModel):
    modulos = models.ForeignKey(
        'Modulo',
        on_delete=models.CASCADE
    )
    titulo = models.CharField(
        null=True,
        max_length=100
    )
    slug = models.SlugField(
        max_length=255,
        unique=True
    )
    order_with_respect_to = 'modulos'
    vimeo_id = models.CharField(
        max_length=32,
        null=True
    )

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse_lazy(
            'modulos:aula', kwargs={'slug': self.slug}
        )

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)

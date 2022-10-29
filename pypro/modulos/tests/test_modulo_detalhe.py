import pytest
from django.urls import reverse_lazy
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula, Modulo


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aulas(modulo):
    return baker.make(Aula, 5, modulos=modulo)


@pytest.fixture
def resp(client, modulo, aulas):
    return client.get(
        reverse_lazy(
            'modulos:detalhe', kwargs={'slug': modulo.slug}
        )
    )


def test_create_modulo(modulo):
    assert modulo.titulo is not None


def test_titulo(resp, modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo):
    assert_contains(resp, modulo.publico)


def test_aulas_titulos(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_aulas_links(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())

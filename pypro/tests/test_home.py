from django.urls import reverse
from django.test import Client
import pytest

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp
    # return client.get(reverse('base:home'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}"')

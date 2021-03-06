import pytest
from pytest_django.fixtures import  django_user_model, transactional_db
import logging

from nsot import models


log = logging.getLogger(__name__)


@pytest.fixture
def user(django_user_model):
    """Create and return a non-admin user."""
    user = django_user_model.objects.create(email='user@localhost')
    return user


@pytest.fixture
def admin_user(django_user_model):
    """Create and return an admin user."""
    user = django_user_model.objects.create(
        email='admin@localhost', is_superuser=True, is_staff=True
    )
    return user


@pytest.fixture
def site():
    site = models.Site.objects.create(
        name='Test Site', description='This is a Test Site.'
    )
    return site

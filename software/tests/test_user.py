import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user_Jibreel(db):
    """Test api url"""
    return User.objects.create_user("Jibreel")


def test_user_check_password(db, user_Jibreel):
    user_Jibreel.set_password("s3cr3t")
    assert user_Jibreel.check_password("s3cr3t") is True


def test_should_not_check_unusable_password(db, user_Jibreel):
    user_Jibreel.set_password("secret")
    user_Jibreel.set_unusable_password()
    assert user_Jibreel.check_password("secret") is False

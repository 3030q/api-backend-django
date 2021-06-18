import pytest
from api.models import CustomUser


# @pytest.fixture()
# def super_user():
#     return CustomUser.objects.get(pk=1)
#
#
# @pytest.mark.django_db
# def test_my_user(super_user):
#     assert super_user.is_superuser


def test_upper():
    assert 'foo'.upper() == 'FOO'

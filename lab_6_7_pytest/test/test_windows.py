import pytest

from src.drivers import WindowsDriver
from src.main import MyClass


@pytest.fixture()
def my_class():
    return MyClass(WindowsDriver)


def test_helper_should_not_have_ls(my_class):
    assert my_class.helper('ls -l') is None


def test_helper_dir(my_class):
    assert my_class.helper('dir /l') == '/l lista ze szczegolami'


def test_helper_ipconfig(my_class):
    expected = ['/? komunikat pomocy', '/all wszysciusienko']
    actual = my_class.helper('ipconfig /? /all').split(', ')
    assert sorted(expected) == sorted(actual)

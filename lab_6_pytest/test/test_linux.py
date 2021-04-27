import pytest

from src.drivers import WindowsDriver, LinuxDriver
from src.main import MyClass


@pytest.fixture()
def my_class():
    return MyClass(LinuxDriver)


def test_helper_should_not_have_dir(my_class):
    assert my_class.helper('dir /a') is None


def test_helper_ls(my_class):
    assert my_class.helper('ls -l') == '-l lista ze szczegolami'

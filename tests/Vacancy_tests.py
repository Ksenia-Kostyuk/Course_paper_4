import pytest
from src.Vacancy import Vacancy

@pytest.fixture
def fix_test():
    return Vacancy('Разработчик','Владикавказ','Разработка приложений', 100, 300, 'RUB', 'http/')

def test_init():
    assert fix_test.__init__() == None


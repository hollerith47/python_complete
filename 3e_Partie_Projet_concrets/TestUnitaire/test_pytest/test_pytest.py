# Test qui permet d'additionner deux nombres
# test qui permet d'additionner deux chaines de caracteres
import pytest
from main_ import add, divide


def test_add_with_two_numbers():
    assert add(5, 10) == 15
    
def test_add_with_two_letters():
    assert add("a", "b") == "ab"
    
def test_add_with_two_booleans():
    assert add(True, False) == 1
    assert add(True, True) == 2
    assert add(False, False) == 0
    
def test_add_with_two_none():
    with pytest.raises(TypeError):
        add(None, None)
    
def test_divide_with_two_numbers():
    assert divide(10, 2) == 5


"""dans notre cas on fait le test avec le module pytest avec son plugin pytest-html (installer aek pip)

# commande pytest
1. python -m pytest test.py
2. python -m pytest test.py -v (pour avoir plus de details)

# pytest-html
1.python -m pytest test_pytest.py -v --html = index.html (on genere le fichier html dans la racine du dossier)

"""

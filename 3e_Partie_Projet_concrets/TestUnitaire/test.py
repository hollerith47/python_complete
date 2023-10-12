# Test qui permet d'additionner deux nombres
# test qui permet d'additionner deux chaines de caracteres

from unittest import TestCase
from main import add, divide


class Test(TestCase):
    def test_add_with_two_numbers(self):
        self.assertEqual(add(5, 10), 15)
    
    def test_add_with_two_letters(self):
        self.assertEqual(add("a", "b"), "ab")
    
    def test_add_with_two_booleans(self):
        self.assertEqual(add(True, False), 1)
        self.assertEqual(add(True, True), 2)
        self.assertEqual(add(False, False), 0)
    
    def test_add_with_two_none(self):
        with self.assertRaises(TypeError):
            add(None, None)
    
    def test_divide_with_two_numbers(self):
        self.assertEqual(divide(10, 2), 5)


"""dans notre cas on fait le test avec le module coverage (installer aek pip)
commande de base
1. coverage run -m unittest test
2. coverage html
3. ouvrir le fichier index.html generer pour avoir resultat des tests.

# commande pytest
1. python -m pytest test.py
2. python -m pytest test.py -v (pour avoir plus de details)

# unittest
1.python -m unittest test.py
2. python -m unittest test.py -v (pour avoir plus de details)

"""

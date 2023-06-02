import unittest
from translator import englishToFrench, frenchToEnglish

class EnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Good Day"), "Bonjour")


class FrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")


unittest.main()
import unittest

from machinetranslation.translator import english_to_french, french_to_english

class EnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Good Day"), "Bonjour")


class FrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
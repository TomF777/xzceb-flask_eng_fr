import unittest

from translator import english_to_french, french_to_english

class TestEnglish2French(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("room"), "Chambre")


class TestFrench2English(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Salle"), "room")

unittest.main()

    
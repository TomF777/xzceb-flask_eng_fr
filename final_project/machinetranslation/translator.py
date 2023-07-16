""" simple translator """
from deep_translator import MyMemoryTranslator

def english_to_french(english_text: str):
    """ function translates english text into french"""
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text: str):
    """ function translates french text into english"""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    return english_text

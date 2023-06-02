from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    A Function that translates English Text to 
    French text
    """
    #write code here
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    A Function that translates French text
    to English text
    """
    #write the code here
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text

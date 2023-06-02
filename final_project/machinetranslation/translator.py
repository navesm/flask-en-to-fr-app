from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
     #write code here
     translator = MyMemoryTranslator(source='en', target='fr')
     frenchText = translator.translate(englishText)
     return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    translator = MyMemoryTranslator(source='fr', target='en')
    englishText = translator.translate(frenchText)
    return englishText
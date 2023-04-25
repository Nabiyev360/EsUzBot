from deep_translator import GoogleTranslator, single_detection

from random import randint


def deeper(text_to_translate):
    try:
        if randint(0, 2) == 2:
            key='d2be4cd1cd7b9e078fd45682f885dbcf'
        else:
            key='1e0fe5812c091d73da8a27032191d59c'
        user_word_lang = single_detection(text_to_translate, api_key=key)
    except:
        user_word_lang = 'en'

    if user_word_lang !='uz':
        translator = GoogleTranslator(target="uzbek")
    else:
        translator = GoogleTranslator(target="english")
    translated_text = translator.translate(text_to_translate)
    return translated_text.capitalize()
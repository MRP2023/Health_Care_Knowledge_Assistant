from googletrans import Translator

translator = Translator()


def translate(text, target):

    if target is None:
        return text

    result = translator.translate(text, dest=target)

    return result.text

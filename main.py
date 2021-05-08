from builtins import print
import pyperclip
from translate import Translator

if __name__ == '__main__':

    copied = pyperclip.paste()
    print(f'Text to be translated: {copied}')

    translator = Translator(to_lang="it")
    translation = translator.translate(copied)
    print(f'Translation: {translation}')

    print('\n')
    print('\n')
    input("Press enter to exit.")
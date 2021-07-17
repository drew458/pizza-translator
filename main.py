from builtins import print
import pyperclip
from translate import Translator
import translators as ts


def main():
    copied = pyperclip.paste()
    print(f'    Text to be translated: {copied}')

    try:
        translation = ts.google(copied, to_language='it')
    except:
        pass
    try:
        translation = ts.bing(copied, to_language='it')
    except:
        try:
            translator = Translator(to_lang="it")
            translation = translator.translate(copied)
        except:
            pass

    print(f'    Translation: {translation}')

    print('\n')
    print('\n')
    input("Press enter to exit.")


if __name__ == '__main__':
    main()

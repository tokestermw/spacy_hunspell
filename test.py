import os

LIB_DIR = '/usr/share/hunspell'

if __name__ == '__main__':
    from hunspell import HunSpell
    hobj = HunSpell(
        os.path.join(LIB_DIR, 'en_US.dic'),
        os.path.join(LIB_DIR, 'en_US.aff'))

    print(hobj.spell('spookie'))
    print(hobj.suggest('spookie'))

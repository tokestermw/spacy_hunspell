from __future__ import unicode_literals

import os

LIB_DIR = '/usr/share/hunspell'

if __name__ == '__main__':
    # -- default hunspell test
    from hunspell import HunSpell
    hobj = HunSpell(
        os.path.join(LIB_DIR, 'en_US.dic'),
        os.path.join(LIB_DIR, 'en_US.aff'))

    assert hobj.spell('spookie') == False
    assert hobj.suggest('spookie')[:5] == \
        ['spookier', 'spookiness', 'spook', 'cookie', 'bookie']

    # -- spacy pipeline test
    import spacy
    from spacy_hunspell import spaCyHunSpell
    nlp = spacy.load('en_core_web_sm')
    hunspell = spaCyHunSpell(nlp, 'linux')
    nlp.add_pipe(hunspell)

    doc = nlp('I can haz cheezeburger.')
    haz = doc[2]
    assert haz._.hunspell_spell == False
    assert haz._.hunspell_suggest[:5] == \
        ['ha', 'haze', 'hazy', 'has', 'hat']
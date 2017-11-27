from __future__ import unicode_literals

import os

DEFAULT_PATH = os.environ.get('DEFAULT_PATH', 'linux')


if __name__ == '__main__':
    # -- spacy pipeline test
    import spacy
    from spacy_hunspell import spaCyHunSpell
    nlp = spacy.load('en_core_web_sm')
    hunspell = spaCyHunSpell(nlp, DEFAULT_PATH)
    nlp.add_pipe(hunspell)

    doc = nlp('I can haz cheezeburger.')
    haz = doc[2]
    assert haz._.hunspell_spell == False
    assert haz._.hunspell_suggest[:5] == \
        ['ha', 'haze', 'hazy', 'has', 'hat']

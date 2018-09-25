from __future__ import unicode_literals

import os

from hunspell import HunSpell

from spacy.tokens import Doc, Span, Token

from spacy_hunspell._about import __version__

DEFAULT_DICTIONARY_PATHS = {
    'mac': '/Library/Spelling',
    'linux': '/usr/share/hunspell',
}

HUNSPELL_PROFILE = os.environ.get('HUNSPELL_PROFILE', 'linux')


class spaCyHunSpell(object):

    name = 'hunspell'

    def __init__(self, nlp, path=HUNSPELL_PROFILE):
        if path in DEFAULT_DICTIONARY_PATHS:
            default_path = DEFAULT_DICTIONARY_PATHS[path]
            dic_path, aff_path = (
                os.path.join(default_path, 'en_US.dic'),
                os.path.join(default_path, 'en_US.aff'),
            )
        else:
            assert len(path) == 2, 'Include two paths: dic_path and aff_path'
            dic_path, aff_path = path

        self.hobj = HunSpell(dic_path, aff_path)

        if not Token.has_extension('hunspell_spell'):
            Token.set_extension('hunspell_spell', default=None)
        if not Token.has_extension('hunspell_suggest'):
            Token.set_extension('hunspell_suggest', getter=self.get_suggestion)

    def __call__(self, doc):
        for token in doc:
            try:
                token._.hunspell_spell = self.hobj.spell(token.text)
            except UnicodeEncodeError:
                pass
        return doc

    def get_suggestion(self, token):
        # TODO: include a lower option?
        # TODO: include suggestion numbers?
        # TODO: include stemmer?
        try:
            suggestions = self.hobj.suggest(token.text)
        except UnicodeEncodeError:
            suggestions = []
        return suggestions

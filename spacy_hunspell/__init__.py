from __future__ import unicode_literals
from pathlib import Path

from hunspell import HunSpell

from spacy.language import Language
from spacy.tokens import Token

from spacy_hunspell._about import __version__


class Hunspell(object):

    name = 'hunspell'

    def __init__(self, nlp: Language, path: str, lang: str='en_US'):
        path = Path.cwd() / path
        
        if not any([nlp, isinstance(nlp, Language)]):
            raise ValueError('nlp must be of a spaCy Language.') from None

        if not path.exists():
            raise NotADirectoryError('{} does not exist.'.format(path)) from None

        dic_path, aff_path = (
            path / '{}.dic'.format(lang),
            path / '{}.aff'.format(lang),
        )

        self.hobj = HunSpell(dic_path, aff_path)

        Token.set_extension('hunspell_spell', default=None)
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

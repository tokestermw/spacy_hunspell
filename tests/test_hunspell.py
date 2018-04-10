import os
import unittest
from unittest import mock

import pytest

from spacy.language import Language

from spacy_hunspell import Hunspell


HUNSPELL = None
NLP = Language()


def test_nlp_integration():
    HUNSPELL = Hunspell(NLP, path='dictionaries')
    NLP.add_pipe(HUNSPELL)
    assert NLP.pipe_names[-1] == 'hunspell'


def test_nlp_integration_with_invalid_path():
    with pytest.raises(NotADirectoryError):
        Hunspell(NLP, path='foo')


def test_nlp_with_no_language():
    with pytest.raises(ValueError):
        Hunspell(None, path='dictionaries')


def test_single_token():
    doc = NLP('haz')
    assert doc[0]._.hunspell_spell is False


def test_entire_sentence():
    doc = NLP('I can haz cheezeburger.')
    assert doc[0]._.hunspell_spell is True
    assert doc[2]._.hunspell_spell is False
    assert 'has' in doc[2]._.hunspell_suggest

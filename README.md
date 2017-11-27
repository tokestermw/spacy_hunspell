## spacy_hunspell: Hunspell extension for spaCy

This package uses the [spaCy 2.0 extensions](https://spacy.io/usage/processing-pipelines#extensions)
to add [Hunspell](http://hunspell.github.io) support for spellchecking.
Inspired from [this discussion here](https://github.com/explosion/spaCy/issues/315#issuecomment-346194645).

## Usage

Add the spaCyHunspell to the spaCy pipeline.

```
import spacy
from spacy_hunspell import spaCyHunSpell

nlp = spacy.load('en_core_web_sm')
hunspell = spaCyHunSpell('mac')
nlp.add_pipe(hunspell)

doc = nlp('I can haz cheezeburger.')
haz = doc[2]
haz._.hunspell_spell  # True
haz._.hunspell_suggest  # []
```

There are two default locations for Hunspell dictionaries for each platform
(`mac`, and `linux`). If there are not you can specify the two files manually.

```
hunspell = spaCyHunSpell('mac')
hunspell = spaCyHunSpell('linux')
hunspell = spaCyHunSpell('en_US.dic', 'en_US.aff')
```

You can find the [English dictionary files here](http://wordlist.aspell.net/dicts/).

## Installation

Installation is a little tricky for [Hunspell](https://github.com/hunspell/hunspell). Make sure to have `python-dev` and `libhunspell-dev` installed
if on a Linux system. For Mac, `brew install hunspell`.

Install both the Python bindings for Hunspell ([`pyhunspell`](https://github.com/blatinier/pyhunspell))
through `pip install hunspell`.

For Mac, you may have to add a few steps before pip installing:

```
export C_INCLUDE_PATH=/usr/local/include/hunspell
ln -s /usr/local/lib/libhunspell-{VERSION_NUMBER}.a /usr/local/lib/libhunspell.a
```

For Mac 10.13 High Sierra, you may have to set the C flags ([issue](https://github.com/blatinier/pyhunspell/issues/33)).

```
CFLAGS=$(pkg-config --cflags hunspell) LDFLAGS=$(pkg-config --libs hunspell) pip install hunspell
```

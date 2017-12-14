## spacy_hunspell: Hunspell extension for spaCy

This package uses the [spaCy 2.0 extensions](https://spacy.io/usage/processing-pipelines#extensions)
to add [Hunspell](http://hunspell.github.io) support for spellchecking.
Inspired from [this discussion here](https://github.com/explosion/spaCy/issues/315#issuecomment-346194645).

## Usage

Add the spaCyHunSpell to the spaCy pipeline.

```
import spacy
from spacy_hunspell import spaCyHunSpell

nlp = spacy.load('en_core_web_sm')
hunspell = spaCyHunSpell(nlp, 'mac')
nlp.add_pipe(hunspell)

doc = nlp('I can haz cheezeburger.')
haz = doc[2]
haz._.hunspell_spell  # False
haz._.hunspell_suggest  # ['ha', 'haze', 'hazy', 'has', 'hat', 'had', 'hag', 'ham', 'hap', 'hay', 'haw', 'ha z']
```

There are two default locations for Hunspell dictionaries for each platform
(`mac`, and `linux`). If there are not you can specify the two files manually.

```
hunspell = spaCyHunSpell(nlp, 'mac')
hunspell = spaCyHunSpell(nlp, 'linux')
hunspell = spaCyHunSpell(nlp, ('en_US.dic', 'en_US.aff'))
```

You can find the [English dictionary files here](http://wordlist.aspell.net/dicts/).

## Installation

You can install the package directly if you have the prerequisites to
install Hunspell. If it errors out, manually install Hunspell (see below).

```
pip install spacy_hunspell
```

Install Hunspell on Linux.

```
sudo apt-get install libhunspell-dev
```

Install Hunspell on Mac.

```
brew install hunspell
```

Install the Python bindings for Hunspell ([`pyhunspell`](https://github.com/blatinier/pyhunspell)):

```
pip install hunspell
```

For Mac, you may have to add a few steps before pip installing:

```
export C_INCLUDE_PATH=/usr/local/include/hunspell
ln -s /usr/local/lib/libhunspell-{VERSION_NUMBER}.a /usr/local/lib/libhunspell.a
```

For Mac 10.13 High Sierra, you may have to set the C flags ([issue](https://github.com/blatinier/pyhunspell/issues/33)).

```
CFLAGS=$(pkg-config --cflags hunspell) LDFLAGS=$(pkg-config --libs hunspell) pip install hunspell
```

Install the rest of the requirements.

```
pip install -r requirements.txt
```

And download at least one spaCy model.

```
python -m spacy download en_core_web_sm
```

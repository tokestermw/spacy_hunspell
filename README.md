# spacy_hunspell: Hunspell extension for spaCy

This package uses the [spaCy 2.0 extensions](https://spacy.io/usage/processing-pipelines#extensions)
to add [Hunspell](http://hunspell.github.io) support for spellchecking.
Inspired from [this discussion here](https://github.com/explosion/spaCy/issues/315#issuecomment-346194645).

## Usage

The default language file is `en_US`. This means that given a `path`, `Hunspell` will search
for `path/language`.

Download the [dictionaries here](https://cgit.freedesktop.org/libreoffice/dictionaries/tree/). You need both `.dic` and `.aff`.

For example, if you use the `de_DE_frami` dictionary files and you stored them in the `dictionaries` folder in your current working directory, you will have to instantiate Hunspell like so:

```
Hunspell(nlp, path='dictionaries', `de_DE_frami`)
```

### Adding Hunspell to the spaCy pipeline 

```python
import spacy
from spacy_hunspell import Hunspell

nlp = spacy.load('en_core_web_sm')
hunspell = Hunspell(nlp, path='dictionaries')  # the directory that your dictionaries are located
nlp.add_pipe(hunspell)

doc = nlp('I can haz cheezeburger.')
haz = doc[2]
haz._.hunspell_spell  # False
haz._.hunspell_suggest  # ['ha', 'haze', 'hazy', 'has', 'hat', 'had', 'hag', 'ham', 'hap', 'hay', 'haw', 'ha z']
```

## Installation

You can install the package directly if you have the prerequisites to
install Hunspell. If it errors out, manually install Hunspell (see below).

```
$ pip install spacy_hunspell
```

## Dependencies

### Linux

```
# sudo apt-get install libhunspell-dev

$ pip install hunspell
```

### macOS

```bash
$ brew install hunspell
$ export C_INCLUDE_PATH=/usr/local/include/hunspell
$ ln -s /usr/local/lib/libhunspell-{VERSION_NUMBER}.a /usr/local/lib/libhunspell.a
```

For Mac 10.13 High Sierra, you may have to set the C flags ([issue](https://github.com/blatinier/pyhunspell/issues/33)). The following install may take a while.

```bash
$ CFLAGS=$(pkg-config --cflags hunspell) LDFLAGS=$(pkg-config --libs hunspell) pip install -r requirements.txt
```

Download at least one spaCy model.

```bash
$ python -m spacy download en_core_web_sm
```

import os

from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


def _read_about():
    with open(os.path.join(ROOT_DIR, 'spacy_hunspell/_about.py'), 'r') as f:
        about = {}
        exec(f.read(), about)

    return about


def _read_readme():
    with open(os.path.join(ROOT_DIR, 'README.md'), 'r') as f:
        readme = f.read()
    return readme


if __name__ == '__main__':
    about = _read_about()
    readme = _read_readme()

    setup(
        name='spacy_hunspell',
        version=about['__version__'],
        description='spaCy extension for Hunspell.',
        long_description=readme,
        url=about['__url__'],
        author=about['__author__'],
        author_email=about['__email__'],
        license='MIT',
        packages=find_packages(),
        install_requires=[
            'spacy>=2.0.0',
            'hunspell==0.5.0',
        ],
        zip_safe=False,
    )

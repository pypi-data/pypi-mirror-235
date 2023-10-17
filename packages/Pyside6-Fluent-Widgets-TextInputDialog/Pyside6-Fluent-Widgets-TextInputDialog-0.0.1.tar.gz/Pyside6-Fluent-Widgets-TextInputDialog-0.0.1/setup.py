import codecs
import os

from setuptools import find_packages, setup

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '0.0.1'
DESCRIPTION = 'It provides a simple way to create text input dialogs.'
LONG_DESCRIPTION = 'TextInputDialog is a library for creating text input dialogs based on Pyside6-Fluent-Widgets. It provides a simple way to create text input dialogs.'

# Setting up
setup(
    name="Pyside6-Fluent-Widgets-TextInputDialog",
    version=VERSION,
    author="Chamiko",
    author_email="Chamiko@foxmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        "PySide6-Fluent-Widgets",
    ],
    keywords=['PySide6', 'Fluent-Widgets'],
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
    python_requires='>=3.6, <3.12',
)
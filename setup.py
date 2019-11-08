# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name         = 'powerline-ext-tmux',
    description  = 'A Powerline extention for tmux',
    version      = '0.0.1',
    keywords     = 'powerline extension tmux',
    license      = 'MIT',
    author       = 'bundai223',
    author_email = 'bundai223@gmail.com',
    url          = 'https://github.com/bundai223/powerline-ext-tmux',
    packages     = setuptools.find_packages(),
    classifiers  = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)

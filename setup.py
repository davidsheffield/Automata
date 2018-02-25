import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    readme = f.read()

setup(name='Automata',
      version='0.1.0',
      description='Cellular automata and related algorithms',
      long_description=readme,
      author='David Sheffield',
      author_email='david@davidsheffield.net',
      url='https://github.com/davidsheffield/Automata',
      packages=['automata'],
      license='GNU GPLv3',
      keywords='cellular automata automaton',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: MacOS X',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python :: 3.6'
      ]
)

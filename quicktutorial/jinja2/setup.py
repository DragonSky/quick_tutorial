__author__ = 'stewartpj'

from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_jinja2'
]

setup(name='tutorial',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
      )

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Time Dev-Brasil'
SITENAME = "Dev-Brasil"
SITEURL = 'https://dev-brasil.github.io/site'
SITESUBTITLE = 'site de programação para iniciantes'

PATH = 'content'
OUTPUT_PATH = 'site' # also in Makefile

THEME = 'themes/attila'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

DEFAULT_DATE = 'fs'
#SUMMARY_MAX_LENGTH = None

#MARKUP = ('md', 'ipynb')
MARKUP = ('md')

DISPLAY_PAGES_ON_MENU = True

PLUGIN_PATHS = [
    'plugins/'
]

PLUGINS = [
    'just_table',
    'liquid_tags.youtube',
    #'liquid_tags.notebook',
    #'ipynb.markup',
    'pin_to_top',
    # 'post_revision',
    #'render_math',
    #'rmd_reader',
    'show_source',
    # 'summary',
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# for post_revision
GITHUB_URL = 'https://github.com/dev-brasil/dev-brasil.github.io'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SHOW_FULL_ARTICLE = True

RMD_READER_KNITR_OPTS_KNIT = None

MARKDOWN = {
        'extensions_configs':
            {
                'markdown.extensions.extra': {},
                'markdown.extensions.meta': {},
                'markdown.extensions.toc': {},
            },
        'extensions': ['extra', 'meta', 'toc']

        }

MATH_JAX = {
    'message_style': None,
}

SHOW_SOURCE_IN_SECTION = True
SHOW_SOURCE_ALL_POSTS = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github','https://github.com/dev-brasil/'),)

DEFAULT_PAGINATION = 11

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

AUTHORS_BIO = {
  "Dev-Brasil": {
    "name": "Equipe Dev-Brasil",
    "cover": "https://avatars2.githubusercontent.com/u/881531?v=3&u=ced26c8fd97409f69ee0237da7b87cce1790fb16&s=700",
    "image": "https://avatars2.githubusercontent.com/u/881531?v=3&u=ced26c8fd97409f69ee0237da7b87cce1790fb16&s=400",
    "website": "https://dev-brasil.github.io",
    "location": "Cyber Space",
    "bio": "Insira alguma bio."
  }
}

# GOOGLE_ANALYTICS = ""

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sonny Torres'
SITENAME = "Sonny's Blog"
SITEURL = 'https://sonnycruz.github.io'
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# index.html
NEST_HEADER_IMAGES = 'background.jpg'
NEST_INDEX_HEADER_TITLE = r"Data Analysis Projects"
NEST_INDEX_HEAD_TITLE = 'Homepage'
NEST_INDEX_HEADER_SUBTITLE = r'Manipulating & Analyzing Data with Programming'
NEST_HEADER_LOGO = '/images/blank.png'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images', 'files']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('rst', 'ipynb', )

GITHUB_USER = 'sonnycruz'
GITHUB_SHOW_USER_LINK = True
GITHUB_SKIP_FORK = True

YEAR_ARCHIVE_SAVE_AS = u'posts/{date:%Y}/index.html'

THEME = r"C:\Users\storres.759NYY1\Desktop\Portfolio\sonnysblog\Lib\site-packages\pelican\themes\nest"

READERS = {'html': None}


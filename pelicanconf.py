#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Etienne'
SITENAME = 'My Blog'
SITEURL = 'etiennepouget.com'

PATH = "content"
STATIC_PATHS = []

THEME = "/home/vifespoir/github/blog/pelican-theme/my-theme"
CSS_FILE = "custom.css"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Plugins - all the plugins are at "C:/tools/python/Lib/pelican-plugins/"
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["photos"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

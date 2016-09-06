#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Etienne'
SITENAME = 'My Blog'

OUTPUT_PATH = '/home/vifespoir/github/blog'
PATH = "content"
STATIC_PATHS = ['images']

THEME_STATIC_DIR = 'static'

THEME = "/home/vifespoir/github/pelican-theme/my-theme"
CSS_FILE = "custom.css"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Projects
LINKS = (('Name Generator', 'https://name-generator.etiennepouget.com'),
         ('Machine Learning', 'https://mlearning.etiennepouget.com'))

# Social widget
SOCIAL = (('LinkedIn', 'https://linkedin.com/in/étienne-pouget-7912295b'),
          ('Github', 'https://github.com/Vifespoir'),
          ('Twitter', 'https://twitter.com/EPouget'))

DEFAULT_PAGINATION = 10

# Plugins - all the plugins are at "C:/tools/python/Lib/pelican-plugins/"
PLUGIN_PATHS = ["/home/vifespoir/github/pelican-plugins"]
PLUGINS = ["photos"]
# PHOTO_LIBRARY = "/home/vifespoir/github/pelican-blog/content/images/"
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

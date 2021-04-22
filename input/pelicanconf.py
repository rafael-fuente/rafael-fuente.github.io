#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Rafael de la Fuente'
SITENAME = 'Simulating Physics'
SITEURL = ''

PATH = 'content'


DEFAULT_LANG = 'en'
TIMEZONE = 'Europe/Madrid'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = './theme/'
ABOUT_PAGE = '/pages/about.html'
#SHOW_ARCHIVES = '/archives.html'


DEFAULT_PAGINATION = 10
PLUGIN_PATHS = ['./plugins']

MARKUP = ['md']
PLUGINS = [
    # ...
    'pelican_youtube',
    'code_include',  # including code blocks
    'sitemap'
    # ...
]



SITEMAP = {
    "exclude": ['tag/', 'category/', 'author/'],
    "format": "xml",
    "priorities": {
        "articles": 1.0,
        "indexes": 0.1,
        "pages": 0.01
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "monthly",
        "pages": "monthly"
    }
}




CODE_DIR = 'downloads/code'

AUTHOR_SAVE_AS = 'rafael-de-la-fuente.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
GITHUB_USERNAME = 'rafael-fuente'
#TWITTER_USERNAME = '__cenit'
#STACKOVERFLOW_ADDRESS = ''
AUTHOR_GMAIL = 'rafael.fuente.herrezuelo@gmail.com'
#AUTHOR_BLOG = 'http://rafael-fuente.github.io'
#AUTHOR_CV = ""
YOUTUBE = 'https://www.youtube.com/channel/UCgmKhcvQ7Xg0Wjq1OVXTDlQ'
ENABLE_MATHJAX = True

SHOW_FEED = False  # Need to address large feeds
DATE_FORMAT = {"en": "%a, %d %b %Y"}
LOCALE = ("usa")
STATIC_PATHS = ['images','downloads','favicon.ico']



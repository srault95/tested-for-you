#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path

import arrow

current = Path(__file__).parent.absolute()

PATH = '../content'

OUTPUT_PATH = str(current.joinpath("output"))

CACHE_CONTENT = True
CACHE_PATH = str(current.joinpath("cache"))
# True: charge à partir du cache les non modifiés
LOAD_CONTENT_CACHE = False

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_PATHS = ['posts']

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
PAGE_PATHS = ['pages']

TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = TAG_URL

CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

ARTICLE_LANG_SAVE_AS = None
DRAFT_LANG_SAVE_AS = None
PAGE_LANG_SAVE_AS = None

USE_FOLDER_AS_CATEGORY = False

PLUGIN_PATHS = [
    str(current.joinpath('plugins')),
    #str(current.joinpath('plugins', 'sitemap'))
]

STATIC_PATHS = [
    str(current.joinpath('extras')),
]

#EXTRA_PATH_METADATA = {
#    'extras/CNAME': {'path': 'CNAME'},
#}

EXTRA_TEMPLATES_PATHS = [
    str(current.joinpath('templates')), #robot.txt
]

DIRECT_TEMPLATES = [
    'index',
    'archives',
    'search',
]

TEMPLATE_PAGES = {
    'robots.txt': 'robots.txt'
}

AUTHOR = 'S2LTIC'
OG_AUTHOR = AUTHOR

#Bootstrap v4.0.0-alpha.5
THEME = str(current.joinpath("themes", "alchemy"))

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = "fr"
DEFAULT_DATE = list(arrow.now().timetuple())[:-3] #[2017, 12, 3, 9, 32, 28]
# 24 Février 2017
DEFAULT_DATE_FORMAT = '%d %B %Y'

# Ne pas descendre trop pour le ratio text/html
DEFAULT_PAGINATION = 10

SITENAME = "Tested For You"

SITEURL = os.getenv('SITEURL', "https://tested-for-you.s2ltic.fr")

SOCIAL_WIDGET_NAME = "Présence sur le net"

SOCIAL_LINKEDIN = 'https://www.linkedin.com/in/st%C3%A9phane-rault-54152627/'
SOCIAL_GITHUB = 'https://github.com/srault95'
SOCIAL_TWITTER = 'https://twitter.com/stephanerault'
SOCIAL_GOOGLE_PLUS = 'https://plus.google.com/u/1/118145941995157130608'
SOCIAL_FACEBOOK = 'https://www.facebook.com/s2ltic.stephane.rault'

SOCIAL = (
    ('LinkedIn', SOCIAL_LINKEDIN),
    ("Github", SOCIAL_GITHUB),
    ("Twitter", SOCIAL_TWITTER),
    ("Google+", SOCIAL_GOOGLE_PLUS),
    ("Facebook", SOCIAL_FACEBOOK)
)

# DISQUS_SITENAME = 'srault95'

ARTICLE_EDIT_LINK = 'https://github.com/srault95/tested-for-you/edit/master/content/posts/%(slug)s.md'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

DISPLAY_TAGS_ON_MENU = True
DISPLAY_TAGS_ON_SIDEBAR = True

# Archives
DISPLAY_RECENT_POSTS_ON_MENU = True
RECENT_POST_COUNT = 10

DISPLAY_TAGS_INLINE = True


# https://github.com/nairobilug/pelican-alchemy
#SITESUBTITLE = "Le mariage du travail et de la passion"
#SITEIMAGE: Image that appears in the header.
#DESCRIPTION: Index HTML head <meta> description.
#LINKS: A list of tuples (Title, URL) for menu links.
#ICONS: A list of tuples (Icon, URL) for icon links.
#PYGMENTS_STYLE: Built-in Pygments style for syntax highlighting.
#HIDE_AUTHORS: Hide the author(s) of an article - useful for single author sites.
#RFG_FAVICONS: Use a Favicon Generator package.

LINKS = [
    #('Search', '/search.html')
]

ICONS = [
    ('search fa-2x', '/search.html')
]

#DISQUS_SITENAME
#GAUGES
#GOOGLE_ANALYTICS
#PIWIK_URL
#PIWIK_SITE_ID

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {
            'permalink': False, #True ajoute le ¶
            'anchorlink': False,
            'baselevel': 1
        },
    },
    'output_format': 'html5',
    # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
    'lazy_ol': False,
}

TYPOGRIFY = True

SUMMARY_MAX_LENGTH = 100

WITH_FUTURE_DATES = False

PLUGINS = [
    'related_posts',
    'tag_cloud',
    'extract_toc',
    'sitemap',
    'tipue_search',
    'thumbnailer',
    'algolia_search'
]

def isnumeric(value):
    return str(value).isnumeric()

JINJA_FILTERS = {
    "isnumeric": isnumeric,
    "to_https": lambda x: ""
}

#---plugin sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,   #default 0.5
        'indexes': 1.0,    #default 0.5
        'pages': 0.5,      #default 0.5
    },
    'changefreqs': {
        'articles': 'weekly', #default monthly
        'indexes': 'daily',   #default daily
        'pages': 'weekly',   #default monthly
    }
}

#---### plugin related_posts
RELATED_POSTS_MAX = 5

#---TWITTER
TWITTER_CARDS = True
TWITTER_USERNAME = "stephanerault"

#---### plugin tipue_search
TIPUE_SEARCH = True

#---### plugin algolia_search
ALGOLIA_APP_ID = os.getenv('ALGOLIA_APP_ID', None)
ALGOLIA_SEARCH_API_KEY = os.getenv('ALGOLIA_SEARCH_API_KEY', None)
ALGOLIA_ADMIN_API_KEY = os.getenv('ALGOLIA_ADMIN_API_KEY', None)
ALGOLIA_INDEX_NAME = 'blog'

#---plugin thumbnailer
IMAGE_PATH = "images"
THUMBNAIL_DIR = "theme/thumbnail"
THUMBNAIL_SIZES = {
    'square': '150',    #mypicture_square.jpg
    'middle': '800x?',   #mypicture_middle.jpg
    'full': '?x?',      #mypicture_full.jpg
}

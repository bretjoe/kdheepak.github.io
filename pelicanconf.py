#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dheepak Krishnamurthy'
SITENAME = u'Dheepak Krishnamurthy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Email', 'mailto:me@kdheepak.com'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-themes/elegant/'

# Plugins and extensions
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid',
                'toc(permalink=true)']
PLUGIN_PATH = ['pelican-plugins'] 
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img',
           'neighbors', 'latex', 'related_posts', 'assets', 'share_post',
           'multi_part']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social
SOCIAL = (
        ('Twitter', 'http://twitter.com/talham_'),
        ('Github', 'http://github.com/talha131'),
        ('GitTip', 'http://gittip.com/talha131'),
        ('Email', 'mailto:talha131@gmail.com'),
          )

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'empty'

# SMO
TWITTER_USERNAME = u'talham_'
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Legal
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> onCrash="Reboot();"</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://oncrashreboot.com" property="cc:attributionName" rel="cc:attributionURL">Talha Mansoor</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO
SITE_DESCRIPTION = u'My name is Talha Mansoor \u2015 a software engineer who gets things done. I am talha131 at Github and @talham_ at twitter. I design and build software products for iOS and OSX. I work on Jump Desktop which is a remote desktop application for iOS, OSX and Android. This is my personal blog.'

# Landing Page
PROJECTS = [
        {
            'name': 'Github',
            'url':
            'https://github.com/kdheepak89',
            'description': 'My Github page'},
        {
            'name': 'Ames Market Test Bed',
            'url':
            'https://kdheepak.com/ames-market-test-bed',
            'description': 'The AMES Market Package is an open source software' 
	' implementation of the AMES Wholesale Power Market Test Bed in Java.'}
            ]
LANDING_PAGE_ABOUT = {'title': 'I’m an engineer.',
'details': """<div itemscope itemtype="http://schema.org/Person"><p>My name is <span itemprop="name">Dheepak Krishnamurthy</span>. I’ve dabbled with mobile application and web development, home automation and photography. I’m currently working towards a Master’s degree in Electrical Engineering.
</p><p> 
<img src="images/coverPicture.jpg" alt="Alt text! And a picture of me!" style="width:100%">
</p><p>
I love visiting and reading up on the history of places. My dream is that one day I’d have travelled to every country in the world (Four down, 192 to go!). I love watching movies and having discussions with friends about them. I’ve been on the seemingly never ending quest of completing IMDb’s top 250 movies of all time (An embarrassingly small 91 down, 159 to go). I love reading books and comic books. I love technology an extraordinarily unusual amount and even occasionally contribute to a technology news and media network. Check them out <a href="https://unleashthephones/" title="UnleashThePhones.com" itemprop="url">here</a>, they are really cool!
</p><p>
On this website, I intend to share interesting projects I’m currently working on or have worked on in the past, also as a way of establishing an archive. If you find anything interesting, feel absolutely free to email me, or contact me on Facebook, Twitter or Google Plus.
</p></div>"""}



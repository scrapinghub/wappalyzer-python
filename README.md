# wappalyzer-python -- UNMAINTAINED
![pypi badge](https://badge.fury.io/py/scrapy-streamitem.png)

Python wrapper for [Wappalizer](https://wappalyzer.com/) (utility that uncovers the technologies used on websites)

**Warning: this package is not maintained anymore.**

Scrapinghub and Javier Casas, the original author, have no plans
to support wappalyzer-python in the foreseeable future
(this includes fixing bugs, supporting upgraded dependencies like PyV8 etc.)

If you are interested in continuing the work, please get in touch
via opensource@scrapinghub.com so that we can discuss transferring ownership
of this repository.

# How to use it

```python
>>> from wappalyzer import Wappalyzer
>>> w = Wappalyzer()

>>> w.analyze('http://wikipedia.org')
{u'Apache': {u'confidence': 100, u'version': u'', u'categories': [u'web-servers']},
u'Varnish': {u'confidence': 100, u'version': u'', u'categories': [u'cache-tools']}}

>>> w.analyze('http://tripadvisor.com')
{u'Apache': {u'confidence': 100, u'version': u'', u'categories': [u'web-servers']},
u'Google Analytics': {u'confidence': 100, u'version': u'', u'categories': [u'analytics']},
u'comScore': {u'confidence': 100, u'version': u'', u'categories': [u'analytics']}}

>>> w.analyze('http://facebook.com')
{u'reCAPTCHA': {u'confidence': 100, u'version': u'', u'categories': [u'captchas']}}
```

You can specify the User-Agent to use:
```python
>>> w.analyze('http://www.google.com', user_agent='your_user_agent')
```

Or analyze from already downloaded pages (in this case you'll need to have the url and response headers too):
```python
>>> w.analyze_from_data(url=the_url, html=the_html, headers=the_response_headers)
```

Apps and Categories are available as dict objects:
```python
>>> w.apps
{u'Google Wallet': {u'website': u'wallet.google.com', u'cats': [41], u'script': [u'checkout\\.google\\.com',
u'wallet\\.google\\.com']}, u'Lockerz Share': ...}

>>> w.categories
{u'42': u'tag-managers', u'48': u'network-storage', u'43': u'paywalls', u'49': u'feed-readers', u'24':
u'rich-text-editors', u'25': u'javascript-graphics', u'26': u'mobile-frameworks', ...}

```


Data can be also updated with the latest version available from the [Wappalyzer Github repo](https://github.com/AliasIO/Wappalyzer):

```python
>>> from wappalyzer import updater
>>> updater.update_all()
```
By default app icons will be updated to the `data/icons` folder, in case you need them somewhere else you can specify the destination folder:

```python
>>> from wappalyzer import updater
>>> updater.update_all(icons_folder='your_icons_folder')
```

Or update them individually:

```python
>>> updater.update_icons(icons_folder='your_icons_folder')
```

# Requirements

* [Requests](https://github.com/kennethreitz/requests)
* [PyV8](https://github.com/okoye/PyV8)
* [lxml](https://github.com/lxml/lxml)

Note for macos users: If you have problems installing PyV8 you can use [PyV8-OS-X](https://github.com/brokenseal/PyV8-OS-X):
```
pip install -e git://github.com/brokenseal/PyV8-OS-X#egg=pyv8
```

# Install

Using setup:

```python
python setup.py install
```

Using pypi:

```python
pip install wappalyzer-python
```



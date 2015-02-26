import os
import logging

import requests
from lxml import html

from . import settings


logger = logging.getLogger(__name__)


def _update_file(url, filename):
    logger.debug('Updating file: %s from %s' % (filename, url))
    r = requests.get(url)
    if r.status_code == 200:
        with open(filename, 'w') as f:
            f.write(r.text)


def _download_icon(url, filename):
    logger.debug('Downloading icon: %s from %s' % (filename, url))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)


def _get_icon_list():
    logger.debug('Fetching icon list...')
    r = requests.get(settings.URL_ICONS)
    tree = html.fromstring(r.text)
    links = tree.xpath(settings.XPATH_ICONS)
    return [link.xpath('text()')[0] for link in links]


def update_apps():
    logger.info('Updating apps...')
    _update_file(url=settings.URL_APPS, filename=settings.FILENAME_APPS_JSON)


def update_js():
    logger.info('Updating js...')
    _update_file(url=settings.URL_WAPPALYZER, filename=settings.FILENAME_WAPPALIZER_JS)
    _update_file(url=settings.URL_DRIVER, filename=settings.FILENAME_DRIVER_JS)


def update_icons(folder=None):
    logger.info('Updating icons...')
    icons = _get_icon_list()
    for icon_name in icons:
        icon_url = settings.URL_ICONS_DOWNLOAD_BASE + icon_name
        icon_filename = os.path.join(folder or settings.PATH_ICONS, icon_name)
        _download_icon(icon_url, icon_filename)
    logger.info('%d icon(s) updated' % len(icons))


def update_all(exclude_icons=False, icons_folder=None):
    update_apps()
    update_js()
    if not exclude_icons:
        update_icons(icons_folder)
from urlparse import urlparse
import logging

import requests
try:
    import PyV8
except ImportError:
    from pyv8 import PyV8
try:
    import json
except ImportError:
    import simplejson as json

from . import settings


logger = logging.getLogger(__name__)


class Wappalyzer(object):

    def __init__(self):
        logger.debug('Initializing Wappalyzer...')
        with open(settings.FILENAME_APPS_JSON, 'r') as f:
            data = json.loads(f.read())
        self.categories = data['categories']
        self.apps = data['apps']

    def analyze(self, url, user_agent=None):
        logger.debug('Fetching: %s' % url)

        response = requests.get(
            url=url,
            headers={'User-Agent': user_agent or settings.USER_AGENT}
        )
        return self.analyze_from_data(
            url=url,
            html=response.text,
            headers=dict(response.headers))

    def analyze_from_data(self, url, html, headers):
        logger.debug('Analyzing: %s' % url)

        ctxt = PyV8.JSContext()
        ctxt.enter()

        with open(settings.FILENAME_WAPPALIZER_JS) as f:
            ctxt.eval(f.read())

        with open(settings.FILENAME_DRIVER_JS) as f:
            ctxt.eval(f.read())

        apps = json.dumps(self.apps)
        categories = json.dumps(self.categories)
        data = {
            'host': urlparse(url).hostname,
            'url': url,
            'html': html,
            'headers': headers
        }

        return json.loads(ctxt.eval(
            "w.apps={apps}; w.categories={categories}; w.driver.data={data}; w.driver.init();".format(
                apps=apps,
                categories=categories,
                data=json.dumps(data)
                )
        ))

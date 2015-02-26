import os

# --------------------------------------------------------
# Remote URLs
# --------------------------------------------------------
# Bases
URL_RAW_SOURCE_BASE = 'https://raw.githubusercontent.com/AliasIO/Wappalyzer/master/src/'
URL_SOURCE_BASE = 'https://github.com/ElbertF/Wappalyzer/tree/master/src/'

# URLs
URL_APPS = URL_RAW_SOURCE_BASE + 'apps.json'
URL_WAPPALYZER = URL_RAW_SOURCE_BASE + 'wappalyzer.js'
URL_DRIVER = URL_RAW_SOURCE_BASE + 'drivers/php/js/driver.js'
URL_ICONS = URL_SOURCE_BASE + 'icons'
URL_ICONS_DOWNLOAD_BASE = URL_RAW_SOURCE_BASE + 'icons/'

# --------------------------------------------------------
# Xpaths
# --------------------------------------------------------
XPATH_ICONS = '//table[@class="files"]//td[@class="content"]//a[contains(text(),".png")]'

# --------------------------------------------------------
# Local Files
# --------------------------------------------------------
# Paths
PATH_DATA = os.path.join(os.path.dirname(__file__), 'data')
PATH_ICONS = os.path.join(PATH_DATA, 'icons')

# Files
FILENAME_APPS_JSON = os.path.join(PATH_DATA, 'apps.json')
FILENAME_WAPPALIZER_JS = os.path.join(PATH_DATA, 'wappalyzer.js')
FILENAME_DRIVER_JS = os.path.join(PATH_DATA, 'driver.js')

# --------------------------------------------------------
# User Agents
# --------------------------------------------------------
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'

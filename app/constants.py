import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(APP_DIR, 'data')
CONFIG_DIR = os.path.join(APP_DIR, 'config')
TITLEDB_DIR = os.path.join(DATA_DIR, 'titledb')
TITLEDB_URL = 'https://github.com/blawar/titledb.git'
TITLEDB_DEFAULT_FILES = [
    'cnmts.json',
    'versions.json',
    'languages.json'
]

OWNFOIL_DB = 'sqlite:////' + os.path.join(CONFIG_DIR, 'ownfoil.db')

DEFAULT_SETTINGS = {
    "library": {
        "path": "/games",
        "region": "US",
        "language": "en"
    },
    "shop": {
        "motd": "Welcome to your own shop!",
        "public": False,
        "encrypt": False,
        "clientCertPub": "-----BEGIN PUBLIC KEY-----",
        "clientCertKey": "-----BEGIN PRIVATE KEY-----"
    }
}

tinfoil_headers = [
    'Theme',
    'Uid',
    'Version',
    'Revision',
    'Language',
    'Hauth',
    'Uauth'
]

ALLOWED_EXTENSIONS = [
    'nsp',
    'nsz',
    'xci',
    'xcz',
]
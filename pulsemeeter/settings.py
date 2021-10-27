import os
import platform


__version__ = '1.2'


HOME = os.getenv('HOME', os.getenv('USERPROFILE'))
CONFIG_HOME = os.getenv('XDG_CONFIG_HOME', os.path.join(HOME, '.config'))
CONFIG_DIR = os.path.join(CONFIG_HOME, 'pulsemeeter')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')
ORIG_CONFIG_FILE = 'lib/python3.9/site-packages/pulsemeeter/config.json'
GLADEFILE = 'lib/python3.9/site-packages/pulsemeeter/Interface.glade'
PIDFILE = '/tmp/pulsemeeter.pid'

OS = platform.uname()[0]
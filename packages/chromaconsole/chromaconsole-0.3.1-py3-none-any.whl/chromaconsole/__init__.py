from .chromaconsole import Color, Style

import subprocess
from pkg_resources import get_distribution
import requests
try:
    version = get_distribution("chromaconsole").version
    latest_version = requests.get(f'https://pypi.org/pypi/chromaconsole/json').json()['info']['version']
    if version != latest_version:
        subprocess.check_call(['pip', 'install', '--upgrade', 'chromaconsole'])
except Exception as e:
    print(f"An error occurred: {e}")
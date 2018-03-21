#!/usr/bin/env python3

import time

from api import get_height
from updater import update_peers


_INTERVAL_SEC = 10
_WATCH_URL = 'http://185.117.73.74:8080'


if __name__ == '__main__':
    height = 0
    while True:
        new_height = get_height(_WATCH_URL)
        if new_height > height:
            print('New block found')
            update_peers()
            height = new_height
        print('Waiting...')
        time.sleep(_INTERVAL_SEC)

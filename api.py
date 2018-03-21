from ipaddress import ip_address
import re
import requests


class Parser(object):
    def __init__(self):
        pass

    def _get_url(self, resp):
        assert len(resp) == 3
        address = resp[1]
        port = resp[2]
        url = 'http://{}.{}.{}.{}:{}'.format(address[1], address[2],
                                             address[3], address[4],
                                             port)
        return url

    def is_global(self, url):
        match = re.match('.*:\/\/(.*):\d+', url)
        address = ip_address(match.group(1))
        return address.is_global

    def get_heights(self, resp):
        return resp[1]

    def get_peers(self, resp):
        peer_rows = resp[1][1:]
        peer_urls = []
        for row in peer_rows:
            url = self._get_url(row)
            if self.is_global(url):
                peer_urls.append(url)
        return peer_urls


# [52,234,133,196,8080], # Mandel
# [159,65,120,84,8080], # Zack

def get_initial_peer_urls():
    lookup_urls = ['http://52.234.133.196:8080',
                   'http://159.65.173.9:8080',
                   'http://159.89.106.253:8080',
                   'http://159.65.120.84:8080']
    urls = get_all_peers(lookup_urls)
    return urls


def get_height(url):
    parser = Parser()
    try:
        response = requests.post(url, '["height"]')
        height = parser.get_heights(response.json())
        print('{:28} height: {:>5}'.format(url, height))
        return height
    except:
        print('{:28} height: {:>5}'.format(url, 'error'))
        return None


def get_heights(urls):
    heights = []
    for url in urls:
        heights.append(get_height(url))
    return heights


def get_all_peers(urls):
    parser = Parser()
    all_peers = []
    for url in urls:
        try:
            response = requests.post(url, '["peers"]')
            response_json = response.json()
            peers = parser.get_peers(response_json)
            print('{} {}'.format(url, len(peers)))
            all_peers += peers
        except:
            print('Could not get from {}'.format(url))

    return list(set(all_peers))

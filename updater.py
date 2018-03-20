#!/usr/bin/env python3

from datetime import datetime

from models import Peer
from models import session

from api import get_height
from api import get_initial_peer_urls


def find_new_peers():
    urls = get_initial_peer_urls()
    for url in urls:
        peer = session.query(Peer).filter_by(url=url).one_or_none()
        if peer is None:
            peer = Peer(url=url)
            session.add(peer)
            session.commit()
            print('Added {}'.format(url))


def update_peers():
    peers = session.query(Peer).all()
    for peer in peers:
        try:
            height = get_height(peer.url)
            peer.height = height
            if height is not None:
                peer.updated_at = datetime.utcnow()
            session.add(peer)
            session.commit()
        except:
            print('Error {}'.format(peer.url))
            session.rollback()

if __name__ == '__main__':
    find_new_peers()
    update_peers()

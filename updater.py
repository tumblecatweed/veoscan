from datetime import datetime

from models import Peer
from models import session

from api import get_height
from api import get_initial_peer_list


def update_peers():
    urls = get_initial_peer_list()
    for url in urls:
        height = get_height(url)
        peer = session.query(Peer).filter_by(url=url).one_or_none()
        if peer is None:
            peer = Peer(url=url)

        peer.height = height
        peer.updated_at = datetime.utcnow()
        session.add(peer)
        session.commit()

if __name__ == '__main__':
    update_peers()

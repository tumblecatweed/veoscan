from flask import Flask
from flask import render_template
from models import Peer
from models import session

app = Flask(__name__)


def get_top_height(peers):
    heights = [p.height if p.height else 0 for p in peers]
    return sorted(heights)[-1]


def get_num_height_peers(height):
    peers = session.query(Peer).filter_by(height=height).all()
    return len(peers)


@app.route('/amoveo-network-status')
def index():
    peers = session.query(Peer).order_by(Peer.height.desc()).order_by(Peer.url.desc()).all()
    top_height = get_top_height(peers)
    num_top_height_peers = get_num_height_peers(top_height)
    return render_template('index.html', peers=peers, top_height=top_height, num_top_height_peers=num_top_height_peers)


@app.route('/donate')
def donate():
    return render_template('donate.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()

from flask import Flask
from flask import render_template
from models import Peer
from models import session

app = Flask(__name__)


@app.route('/')
def index():
    peers = session.query(Peer).order_by(Peer.height.desc()).order_by(Peer.url.desc()).all()
    return render_template('index.html', peers=peers)


if __name__ == '__main__':
    app.run()

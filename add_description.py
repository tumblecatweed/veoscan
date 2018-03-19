#!/usr/bin/env python3

import argparse

from models import Peer 
from models import session 


parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--description')
args = parser.parse_args()

url = args.url
description = args.description

p = session.query(Peer).filter_by(url=url).one()
p.description = description

session.add(p)
session.commit()

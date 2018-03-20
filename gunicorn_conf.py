import multiprocessing


# Server Socket
bind = 'unix:/tmp/gunicorn_veoscan.sock'
backlog = 2048


# Worker Processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 0
timeout = 30
keepalive = 2
debug = False
spew = False


# Logging
accesslog = '/var/log/gunicorn/veoscan/access.log'
errorlog = '/var/log/gunicorn/veoscan/error.log'
log_level = 'info'


# Process Name
proc_name = 'gunicorn_veoscan'

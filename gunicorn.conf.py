# gunicorn_config.py
bind = "0.0.0.0:443"
workers = 4
threads = 2
worker_class = "gthread"
timeout = 120
keyfile = '/etc/letsencrypt/live/blsh-api.northwindsoftware.com/privkey.pem '
certfile = '/etc/letsencrypt/live/blsh-api.northwindsoftware.com/fullchain.pem'


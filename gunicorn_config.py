# gunicorn_config.py
bind = "0.0.0.0:8000"
workers = 4
threads = 2
worker_class = "gthread"
timeout = 120


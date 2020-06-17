web: gunicorn taleem.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=taleem -B --loglevel=info

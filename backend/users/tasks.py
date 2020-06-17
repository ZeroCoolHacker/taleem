from django.core import management

from taleem import celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')

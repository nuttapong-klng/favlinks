import requests
from celery.schedules import crontab
from django.db import transaction

from config.celery_app import app

from .models import FavoriteUrl


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute="*"), validate_urls.s())


@app.task
def validate_urls():
    favorite_urls = FavoriteUrl.objects.select_for_update()
    with transaction.atomic():
        for favorite_url in favorite_urls:
            try:
                response = requests.get(favorite_url.url, timeout=5)
                favorite_url.url_valid = response.ok
            except requests.RequestException:
                favorite_url.url_valid = False
            favorite_url.save(update_fields=["url_valid"])

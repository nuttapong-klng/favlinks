import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FavoriteUrlsConfig(AppConfig):
    name = "favlinks.favorite_urls"
    verbose_name = _("Favorite URLs")

    def ready(self):
        with contextlib.suppress(ImportError):
            import favlinks.favorite_urls.signals  # noqa: F401

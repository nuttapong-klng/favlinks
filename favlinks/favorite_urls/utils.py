from django.views import defaults as default_views

from favlinks.favorite_urls.models import FavoriteUrl


def get_and_validate_ownership_of_favorite_url(request, favorite_url_id):
    error = False
    error_view = None
    favorite_url = FavoriteUrl.objects.filter(
        id=favorite_url_id,
    ).first()
    if not favorite_url:
        error = True
        error_view = default_views.page_not_found(
            request,
            Exception("Favorite URL not found"),
        )
    elif favorite_url.owner != request.user:
        error = True
        error_view = default_views.permission_denied(
            request,
            Exception("You are not the owner of this favorite URL"),
        )
    return favorite_url, error, error_view

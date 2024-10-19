from django.views import defaults as default_views


def get_and_validate_ownership(request, model, instance_id):
    error = False
    error_view = None
    instance = model.objects.filter(
        id=instance_id,
    ).first()
    if not instance:
        error = True
        error_view = default_views.page_not_found(
            request,
            Exception("Favorite URL not found"),
        )
    elif instance.owner != request.user:
        error = True
        error_view = default_views.permission_denied(
            request,
            Exception("You are not the owner of this favorite URL"),
        )
    return instance, error, error_view

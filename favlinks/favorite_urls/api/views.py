from rest_framework import permissions
from rest_framework import viewsets

from favlinks.favorite_urls.api.serializers import FavoriteUrlSerializer
from favlinks.favorite_urls.models import FavoriteUrl


class FavoriteUrlViewSet(viewsets.ModelViewSet):
    queryset = FavoriteUrl.objects.none()
    serializer_class = FavoriteUrlSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            FavoriteUrl.objects.filter(
                owner=self.request.user,
            )
            .select_related(
                "category",
            )
            .prefetch_related(
                "tags",
            )
        )

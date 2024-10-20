from rest_framework import permissions
from rest_framework import viewsets

from favlinks.favorite_urls.api.filters import CategoryFilter
from favlinks.favorite_urls.api.filters import FavoriteUrlFilter
from favlinks.favorite_urls.api.filters import TagFilter
from favlinks.favorite_urls.api.serializers import CategorySerializer
from favlinks.favorite_urls.api.serializers import FavoriteUrlSerializer
from favlinks.favorite_urls.api.serializers import TagSerializer
from favlinks.favorite_urls.models import Category
from favlinks.favorite_urls.models import FavoriteUrl
from favlinks.favorite_urls.models import Tag


class FavoriteUrlViewSet(viewsets.ModelViewSet):
    queryset = FavoriteUrl.objects.none()
    serializer_class = FavoriteUrlSerializer
    filterset_class = FavoriteUrlFilter
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
            .order_by(
                "-created_at",
            )
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.none()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Category.objects.filter(
                owner=self.request.user,
            )
            .prefetch_related(
                "favorite_urls",
            )
            .order_by(
                "-id",
            )
        )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.none()
    serializer_class = TagSerializer
    filterset_class = TagFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Tag.objects.filter(
                owner=self.request.user,
            )
            .prefetch_related(
                "favorite_urls",
            )
            .order_by(
                "-id",
            )
        )

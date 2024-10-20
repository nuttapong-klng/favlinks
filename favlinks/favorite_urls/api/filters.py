from django_filters import FilterSet
from django_filters import OrderingFilter
from django_filters import filters

from favlinks.favorite_urls.models import Category
from favlinks.favorite_urls.models import FavoriteUrl
from favlinks.favorite_urls.models import Tag


class FavoriteUrlFilter(FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = FavoriteUrl
        fields = [
            "title",
            "url",
            "category",
            "tags",
            "url_valid",
            "created_at",
            "updated_at",
        ]

    order_by = OrderingFilter(
        fields=[
            "id",
            "title",
            "created_at",
            "updated_at",
        ],
    )


class CategoryFilter(FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Category
        fields = [
            "name",
        ]

    order_by = OrderingFilter(
        fields=[
            "id",
            "name",
        ],
    )


class TagFilter(FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Tag
        fields = [
            "name",
        ]

    order_by = OrderingFilter(
        fields=[
            "id",
            "name",
        ],
    )

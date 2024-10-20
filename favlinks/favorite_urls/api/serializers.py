from rest_framework import serializers

from favlinks.favorite_urls.models import Category
from favlinks.favorite_urls.models import FavoriteUrl
from favlinks.favorite_urls.models import Tag


class CategoryCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class TagCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
        ]


class FavoriteUrlSerializer(serializers.ModelSerializer):
    category = CategoryCompactSerializer(read_only=True)
    tags = TagCompactSerializer(many=True, read_only=True)

    class Meta:
        model = FavoriteUrl
        fields = [
            "id",
            "url",
            "title",
            "category",
            "tags",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["owner"] = user
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "favorite_urls_count",
        ]

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["owner"] = user
        return super().create(validated_data)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "favorite_urls_count",
        ]

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["owner"] = user
        return super().create(validated_data)

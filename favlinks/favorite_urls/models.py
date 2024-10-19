from django.db import models


class FavoriteUrl(models.Model):
    url = models.URLField()
    title = models.TextField()
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="favorite_urls",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        related_name="favorite_urls",
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        "Tag",
        related_name="favorite_urls",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="categories",
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tags",
    )

    def __str__(self):
        return self.name

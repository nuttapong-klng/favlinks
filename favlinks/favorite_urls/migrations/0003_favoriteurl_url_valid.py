# Generated by Django 5.0.9 on 2024-10-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_urls', '0002_category_favoriteurl_category_tag_favoriteurl_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteurl',
            name='url_valid',
            field=models.BooleanField(default=None, null=True),
        ),
    ]

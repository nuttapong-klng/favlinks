from django.urls import path

from .views import favorite_url_create_view
from .views import favorite_url_edit_view
from .views import favorite_url_list_view

app_name = "favorite_urls"
urlpatterns = [
    path("create/", view=favorite_url_create_view, name="create"),
    path("edit/<int:id>/", view=favorite_url_edit_view, name="edit"),
    path("list/", view=favorite_url_list_view, name="list"),
]

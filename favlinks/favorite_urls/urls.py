from django.urls import path

from .views import category_create_view
from .views import category_delete_view
from .views import category_edit_view
from .views import category_list_view
from .views import favorite_url_create_view
from .views import favorite_url_delete_view
from .views import favorite_url_edit_view
from .views import favorite_url_list_view

app_name = "favorite_urls"
urlpatterns = [
    path("create/", view=favorite_url_create_view, name="create"),
    path("delete/<int:id>/", view=favorite_url_delete_view, name="delete"),
    path("edit/<int:id>/", view=favorite_url_edit_view, name="edit"),
    path("list/", view=favorite_url_list_view, name="list"),
    path("category/create/", view=category_create_view, name="category-create"),
    path(
        "category/delete/<int:id>/",
        view=category_delete_view,
        name="category-delete",
    ),
    path("category/edit/<int:id>/", view=category_edit_view, name="category-edit"),
    path("category/list/", view=category_list_view, name="category-list"),
]

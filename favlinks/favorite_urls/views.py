from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from favlinks.favorite_urls.forms import CategoryForm
from favlinks.favorite_urls.forms import FavoriteUrlForm
from favlinks.favorite_urls.models import Category
from favlinks.favorite_urls.models import FavoriteUrl
from favlinks.favorite_urls.utils import get_and_validate_ownership


class FavoriteUrlCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = FavoriteUrlForm()
        context = {
            "form": form,
            "action": "Create",
        }
        return render(request, "favorite_urls/favoriteurl_create.html", context)

    def post(self, request, *args, **kwargs):
        form = FavoriteUrlForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect("favorite_urls:list")
        return None


class FavoriteUrlDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        favorite_url, error, error_view = get_and_validate_ownership(
            request,
            FavoriteUrl,
            kwargs["id"],
        )
        if error:
            return error_view
        favorite_url.delete()
        return redirect("favorite_urls:list")


class FavoriteUrlEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        favorite_url, error, error_view = get_and_validate_ownership(
            request,
            FavoriteUrl,
            kwargs["id"],
        )
        if error:
            return error_view
        form = FavoriteUrlForm(instance=favorite_url)
        context = {
            "form": form,
            "action": "Edit",
        }
        return render(request, "favorite_urls/favoriteurl_create.html", context)

    def post(self, request, *args, **kwargs):
        favorite_url, error, error_view = get_and_validate_ownership(
            request,
            FavoriteUrl,
            kwargs["id"],
        )
        if error:
            return error_view
        form = FavoriteUrlForm(request.POST, instance=favorite_url)
        if form.is_valid():
            form.save()
            return redirect("favorite_urls:list")
        return None


class FavoriteUrlListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {"favorite_urls": FavoriteUrl.objects.filter(owner=request.user)}
        return render(request, "favorite_urls/favoriteurl_list.html", context)


class CategoryCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        context = {
            "form": form,
            "action": "Create",
        }
        return render(request, "favorite_urls/category_create.html", context)

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect("favorite_urls:category-list")
        return None


class CategoryDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        favorite_url, error, error_view = get_and_validate_ownership(
            request,
            Category,
            kwargs["id"],
        )
        if error:
            return error_view
        favorite_url.delete()
        return redirect("favorite_urls:category-list")


class CategoryEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        favorite_url, error, error_view = get_and_validate_ownership(
            request,
            Category,
            kwargs["id"],
        )
        if error:
            return error_view
        form = CategoryForm(instance=favorite_url)
        context = {
            "form": form,
            "action": "Edit",
        }
        return render(request, "favorite_urls/category_create.html", context)

    def post(self, request, *args, **kwargs):
        favorite_url, error, error_view = get_and_validate_ownership(
            request,
            Category,
            kwargs["id"],
        )
        if error:
            return error_view
        form = CategoryForm(request.POST, instance=favorite_url)
        if form.is_valid():
            form.save()
            return redirect("favorite_urls:category-list")
        return None


class CategoryListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            "categories": Category.objects.filter(
                owner=request.user,
            ).prefetch_related("favorite_urls"),
        }
        return render(request, "favorite_urls/category_list.html", context)


favorite_url_create_view = FavoriteUrlCreateView.as_view()
favorite_url_delete_view = FavoriteUrlDeleteView.as_view()
favorite_url_edit_view = FavoriteUrlEditView.as_view()
favorite_url_list_view = FavoriteUrlListView.as_view()

category_create_view = CategoryCreateView.as_view()
category_delete_view = CategoryDeleteView.as_view()
category_edit_view = CategoryEditView.as_view()
category_list_view = CategoryListView.as_view()

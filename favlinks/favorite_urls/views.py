from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from favlinks.favorite_urls.forms import FavoriteUrlForm
from favlinks.favorite_urls.models import FavoriteUrl
from favlinks.favorite_urls.utils import get_and_validate_ownership_of_favorite_url


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
        favorite_url, error, error_view = get_and_validate_ownership_of_favorite_url(
            request,
            kwargs["id"],
        )
        if error:
            return error_view
        favorite_url.delete()
        return redirect("favorite_urls:list")


class FavoriteUrlEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        favorite_url = FavoriteUrl.objects.get(id=kwargs["id"], owner=request.user)
        form = FavoriteUrlForm(instance=favorite_url)
        context = {
            "form": form,
            "action": "Edit",
        }
        return render(request, "favorite_urls/favoriteurl_create.html", context)

    def post(self, request, *args, **kwargs):
        favorite_url = FavoriteUrl.objects.get(id=kwargs["id"], owner=request.user)
        form = FavoriteUrlForm(request.POST, instance=favorite_url)
        if form.is_valid():
            form.save()
            return redirect("favorite_urls:list")
        return None


class FavoriteUrlListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {"favorite_urls": FavoriteUrl.objects.filter(owner=request.user)}
        return render(request, "favorite_urls/favoriteurl_list.html", context)


favorite_url_create_view = FavoriteUrlCreateView.as_view()
favorite_url_delete_view = FavoriteUrlDeleteView.as_view()
favorite_url_edit_view = FavoriteUrlEditView.as_view()
favorite_url_list_view = FavoriteUrlListView.as_view()

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from favlinks.favorite_urls.forms import FavoriteUrlForm


class FavoriteUrlCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = FavoriteUrlForm()
        context = {"form": form}
        return render(request, "favorite_urls/favoriteurl_create.html", context)

    def post(self, request, *args, **kwargs):
        form = FavoriteUrlForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect("/")
        return None


favorite_url_create_view = FavoriteUrlCreateView.as_view()

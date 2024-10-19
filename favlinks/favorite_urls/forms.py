from django import forms

from .models import FavoriteUrl


class FavoriteUrlForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = FavoriteUrl
        fields = [
            "title",
            "url",
        ]

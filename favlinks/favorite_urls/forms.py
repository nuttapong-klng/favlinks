from django import forms

from .models import Category
from .models import FavoriteUrl
from .models import Tag


class FavoriteUrlForm(forms.ModelForm):
    title = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = FavoriteUrl
        fields = [
            "title",
            "url",
            "category",
            "tags",
        ]

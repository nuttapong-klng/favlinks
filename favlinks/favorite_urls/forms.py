from django import forms

from .models import Category
from .models import FavoriteUrl
from .models import Tag


class FavoriteUrlForm(forms.ModelForm):
    title = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = FavoriteUrl
        fields = [
            "title",
            "url",
            "category",
            "tags",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
        ]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            "name",
        ]

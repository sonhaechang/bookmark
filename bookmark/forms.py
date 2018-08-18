from django import forms
from bookmark.models import Bookmark

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['site_name', 'url']

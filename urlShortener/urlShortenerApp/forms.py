from django import forms

class URLShortenerForm(forms.Form):
    url = forms.URLField()

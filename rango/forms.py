from django import forms
from rango.models import Page, Category


class CategoryForm(forms.ModelForm):
    'Create Category Form'
    name = forms.CharField(
        max_length=128, help_text="Please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    'Create Page Form'
    title = forms.CharField(
        max_length=128, help_text="Please enter the title name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    url = forms.CharField(
        max_length=200, help_text="Please Enter the URL of the page")

    class Meta:
        model = Page
        fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data

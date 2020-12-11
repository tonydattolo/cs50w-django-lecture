from django import forms
from django.core.files.utils import FileProxyMixin

from .models import Article


class ArticleForm(forms.ModelForm):
    title   = forms.CharField(
                        label="Article Title",
                        widget=forms.TextInput(
                            attrs={
                               "placeholder": "Article Title"
                            }
                        ))
    content = forms.CharField(
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "blog content goes here",
                                "class": "class-names mb-2",
                                "id": "createArticleFormTextbox",
                                "rows": 10,
                                "cols": 20
                            })) #change to text area through widget prop, .TextField doesn't exist for form
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]

    # def clean_article(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     wanted = "whatever"
    #     if not wanted in title:
    #         raise forms.ValidationError(f"title must include{wanted}")
    #     if not "somethingElse" in title:
    #         raise forms.ValidationError("must include somethingElse")
    #     return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith(".edu"):
    #         raise forms.ValidationError("not a valid student email")
    #     return email

class RawArticleForm(forms.Form):
    title   = forms.CharField(
                        label="Article Title",
                        widget=forms.TextInput(
                            attrs={
                               "placeholder": "Article Title"
                            }
                        ))
    article = forms.CharField(
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "blog content goes here",
                                "class": "class-names mb-2",
                                "id": "createArticleFormTextbox",
                                "rows": 10,
                                "cols": 20
                            })) #change to text area through widget prop, .TextField doesn't exist for form
    
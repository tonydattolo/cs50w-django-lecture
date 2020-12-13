from django import forms

from .models import Entry

class EntryForm(forms.ModelForm):
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
                                "placeholder": "wiki content goes here",
                                "class": "",
                                "id": "createArticleFormTextbox"
                                # "rows": 5,
                                # "cols": 4
                            })) #change to text area through widget prop, .TextField doesn't exist for form
    class Meta:
        model = Entry
        fields = [
            'title',
            'content'
        ]
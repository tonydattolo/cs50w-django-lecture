from django import forms

from .models import Entry

class SearchForm(forms.Form):
    q = forms.CharField(label="Search", max_length=50)

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
    
    # custom form validation
    # def clean_<myFieldName>():
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "cfe" in title:
    #         raise forms.ValidationError("this is not a valid title! must contain 'cfe' ")
    #     if not "whatever" in title:
    #         raise forms.ValidationError("error: title must contain 'whatever' ")
    #     return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.contains(".edu"):
    #         raise form.ValidationError("must be a student email address!")
    #     return email
from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title",
                }
            )) #required is TRUE by default

    content = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Define your products",
                "rows": 20,
                "cols": 30
                }
            )
        )
            
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "küfür" in title:
            raise forms.ValidationError("This is not a valid Title")
        
        return title

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if "küfür" in content:
            raise forms.ValidationError("This is not a valid content")
        return content
            

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title",
                }
            )) #required is TRUE by default

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Define your products",
                "rows": 20,
                "cols": 30
                }
            )
        )

    price = forms.DecimalField(initial=199.99)

    email = forms.EmailField()
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'email'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid Title")
        
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email
            
        
#DON'T NEED TO USE THIS AS FORM
class RawProductForm (forms.Form):
    title = forms.CharField() #required is TRUE by default
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                
                "placeholder": "Define your products",
                "rows": 20,
                "cols": 30

                }
            )
        )
    price = forms.DecimalField(initial=199.99)
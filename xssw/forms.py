from django import forms

class xssurl(forms.Form):
    url=forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete':'off'})
        )
    


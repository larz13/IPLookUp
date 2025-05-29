from django import forms

class IpForm(forms.Form):
    ip = forms.CharField(
        label='',
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'X.X.X.X',
            'class': 'form-control'
        })
    )
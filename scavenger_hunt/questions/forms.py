from django import forms


class Task1Form(forms.Form):
    answer = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your answer here'})
    )

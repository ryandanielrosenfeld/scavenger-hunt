from django import forms


class InputForm(forms.Form):
    answer = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your answer here'})
    )


class ChoiceForm(forms.Form):
    answer = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your answer here'})
    )

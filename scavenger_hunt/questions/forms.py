from django import forms


class InputForm(forms.Form):
    answer = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your answer here'})
    )


TASK2_CHOICES = (
    ('EC', 'An Electric Guitar'),
    ('HB', 'A hoverboard'),
    ('JE', 'A Jet Engine'),
    ('R', 'A Rotunda'),
)


class Task2ChoiceForm(forms.Form):
    answer = forms.ChoiceField(
        label='',
        choices=TASK2_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


TASK9_CHOICES = (
    ('P', 'Plastic'),
    ('C', 'Concrete'),
    ('W', 'Wood'),
    ('M', 'Metal'),
)


class Task9ChoiceForm(forms.Form):
    answer = forms.ChoiceField(
        label='',
        choices=TASK9_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    password = forms.CharField(
        label='',
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'last name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'form-control'})
    )
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control'}),
        label='',
    )
    conf_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'confirm password', 'class': 'form-control'}),
        label='',
    )

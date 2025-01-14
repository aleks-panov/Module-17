from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Ведите логин")
    password = forms.CharField(min_length=8, label="Ведите пароль")
    repeat_password = forms.CharField(min_length=8, label="Повторите пароль")
    age = forms.CharField(max_length=3, label="Введите возраст")
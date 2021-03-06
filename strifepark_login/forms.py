from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
import hashlib
from django.utils.translation import ugettext_lazy as _
from strifepark_login.models import spUserProfile

class ResetForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        try:
            password1 = self.cleaned_data["password1"]
        except KeyError:
            raise forms.ValidationError(_("The two password fields didn't match."))
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2

class ForgotForm(forms.Form):
    username = forms.RegexField(max_length = 25, regex=r'^[\w+]')
    class Meta:
        model = User
        fields = ("username",)
    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(_("The given Username does not exist"))

class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'input-medium',}),max_length = 10)
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'input-medium',}))
    remember = forms.BooleanField(required=False)
class RegisterForm(forms.Form):
    username = forms.RegexField(max_length = 25, regex=r'[\w+]')
    first_name = forms.CharField(max_length = 60)
    last_name = forms.CharField(max_length = 60)
    email = forms.EmailField()
    password1 = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            user.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_("That username already exists."))
    def clean_password2(self):
        try:
            password1 = self.cleaned_data["password1"]
        except KeyError:
            raise forms.ValidationError(_("The two password fields didn't match."))
        password2 = self.cleaned_data["password2"]    
        if password1 != password2: 
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2
    
    def save(self, commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email=(self.cleaned_data["email"])
        user.first_name=(self.cleaned_data["first_name"])
        user.last_name = (self.cleaned_data["last_name"])
        if commit:
            user.save()
        return user    

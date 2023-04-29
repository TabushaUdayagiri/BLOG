from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from app1.models import post



class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Re-Enter_Passward',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']  
        labels = {'email':'Email'}


class UpdateUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login','is_active']
        label = {'email':'Email'}


class UpdateAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        label = {'email':'Email'}

class postform(forms.ModelForm):
    class Meta:
        model = post
        fields = ['id','title','description','posted_date','user_id']
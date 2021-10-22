from django import forms
from django.contrib.auth import authenticate,get_user_model
from django.forms import fields

User=get_user_model()


class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean( self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        passsword=self.cleaned_data.get('password')

        if username and passsword:
            user=authenticate(username=username,passsword=passsword)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(passsword):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('THis user is not active')
        return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegistrationForm(forms.ModelForm):
    email=forms.EmailField(label='Email Address')
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'email2',
            'password'
        ]
    def clean(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        email2=self.cleaned_data.get('email2')
        if email !=email2:
            raise forms.ValidationError('Emails must match')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('THis email is already in use')
        return super(UserRegistrationForm,self).clean(*args,**kwargs)
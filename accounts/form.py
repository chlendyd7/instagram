from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm
)
from .models import User


# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',]
    
    def clean_email(self): #이메일 중복 막기
        email = self.cleaned_data('email')
        if email:
            qs = User.objects.filter(email=email) #유저 모델에서 검색
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소 입니다.")
        return email



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar','first_name', 'last_name', 'website_url', 'bio', 'phone_number', 'gender']
    
class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password2(self):
        old_password = self.cleaned_data.get('old_password')
        new_password2 = super().clean_new_password2()
        if old_password == new_password2:
            raise forms.ValidationError("새로운 암호는 기존 암호와 다르게 입력해주세요.")
        return new_password2
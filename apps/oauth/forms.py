# -*- coding: utf-8 -*-
from django import forms
from .models import Ouser


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Ouser
        fields = ['nickname', 'link', 'avatar']
        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': '建议修改满意的昵称'}),
        }

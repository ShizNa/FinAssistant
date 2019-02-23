from django import forms
from django.core.exceptions import ValidationError

from .models import *


# todo разобраться с филдами
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['object_name', 'description', 'type', 'amount', 'balance', 'ccy']

        # todo add placeholder in every input
        widgets = {
            # todo override lable to Title
            'object_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            # todo create slider (range)
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'balance': forms.Select({
                'class': 'form-control'
            }),
            'ccy': forms.Select(attrs={
                'class': 'form-control'
            }),
            # todo create radio batton
            'type': forms.RadioSelect(attrs={
                'class': 'form-check form-check-inline',
            }),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'add':
            raise ValidationError('Slug may not be ' + new_slug)

        if Account.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug is already exist')

        return new_slug


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['object_name', 'description', 'ccy']
        # todo add placeholder in every input
        widgets = {
            # todo override lable to Title
            'object_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'ccy': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'add':
            raise ValidationError('Slug may not be ' + new_slug)

        if Account.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug is already exist')

        return new_slug

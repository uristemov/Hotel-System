# from urllib import request
# from django.forms import ModelForm
from .models import Card, HotelOrders
from django import forms

class CardCreate(forms.ModelForm):
        card_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Card Number",
                "class": "form-control"
            }
        ))
        card_cvv = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "CVC",
                "class": "form-control"
            }
        ))
        card_month = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "MM",
                "class": "form-control"
            }
        ))
        card_year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "YYYY",
                "class": "form-control"
            }
        ))
        # user = request.user.id
        class Meta:
            model = Card
            fields = ('card_number', 'card_cvv', 'card_month', 'card_year')

class HotelOrderCreate(forms.ModelForm):
        # card_number = forms.CharField(
        # widget=forms.TextInput(
        #     attrs={
        #         "placeholder": "Card Number",
        #         "class": "form-control"
        #     }
        # ))
        # card_cvv = forms.IntegerField(
        # widget=forms.NumberInput(
        #     attrs={
        #         "placeholder": "CVC",
        #         "class": "form-control"
        #     }
        # ))
        class Meta:
            model = HotelOrders
            fields = '__all__'
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone_number', 'additional_info', 'items', 'quantities']
        widgets = {
            'items': forms.HiddenInput(),
            'quantities': forms.HiddenInput(),
        }

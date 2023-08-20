from django import forms
from .models import Customer, MeterReading  # Import both Customer and MeterReading models

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_number', 'name', 'address')

class MeterReadingForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label="Select a customer")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = MeterReading
        fields = ['customer', 'date', 'meter_reading']

class InvoiceForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    amount = forms.DecimalField()

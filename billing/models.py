from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    customer_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    
    class Meta:
        app_label = 'billing'
        
class MeterReading(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    meter_reading = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'billing'

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'billing'
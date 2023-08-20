from django.shortcuts import render, redirect
from .models import Customer, Invoice, MeterReading
from .forms import CustomerForm, MeterReadingForm
from django.db.models import F

# def home(request):
#     customers = Customer.objects.all()
#     latest_meter_readings = MeterReading.objects.select_related('customer').order_by('-date')[:5]
#     context = {'customers': customers, 'latest_meter_readings': latest_meter_readings}
#     return render(request, 'billing/home.html', context)

def home(request):
    customers = Customer.objects.all()
    latest_meter_readings = MeterReading.objects.select_related('customer').order_by('-date')[:5]
    # print("latest_meter_readings =>>>", latest_meter_readings) 
    context = {'customers': customers, 'latest_meter_readings': latest_meter_readings}
    return render(request, 'billing/home.html', context)

#views.py 
from django.db.models import Sum
from django.db.models import F
from decimal import Decimal, InvalidOperation


def admin_home(request):
    default_unit_price = 5

    if request.method == 'POST':
        unit_price = request.POST.get('unit_price')
        if unit_price is not None:
            try:
                unit_price = Decimal(unit_price)
                # Calculate the new due amounts based on the new unit price
                customers = Customer.objects.all()
                for customer in customers:
                    customer.due_amount = customer.due_amount / default_unit_price * unit_price
                    customer.save()
            except (ValueError, InvalidOperation):
                pass

    customers = Customer.objects.all()
    latest_meter_readings = MeterReading.objects.select_related('customer').order_by('-date')[:5]
    
    context = {
        'customers': customers,
        'default_unit_price': default_unit_price,
        'latest_meter_readings': latest_meter_readings
    }
    return render(request, 'billing/admin_home.html', context)

# def admin_home(request):
#     default_unit_price = 5 

#     if request.method == 'POST':
#         unit_price = request.POST.get('unit_price')
#         if unit_price is not None:
#             try:
#                 unit_price = Decimal(unit_price)
#                 # Update the due amounts of customers
#                 Customer.objects.update(due_amount=F('due_amount') * unit_price)
#             except (ValueError, InvalidOperation) as e:
#                 print(f"Error processing unit price: {e}")
#                 pass  # Handle the error here

#     customers = Customer.objects.all()
#     latest_meter_readings = MeterReading.objects.select_related('customer').order_by('-date')[:5]
    
#     context = {
#         'customers': customers,
#         'default_unit_price': default_unit_price,
#         'latest_meter_readings': latest_meter_readings
#     }
#     return render(request, 'billing/admin_home.html', context)

# def admin_home(request):
#     default_unit_price = 5  # Default unit price, can be retrieved from a database or settings
#     if request.method == 'POST':
#         unit_price = request.POST.get('unit_price')
#         if unit_price is not None:
#             try:
#                 unit_price = float(unit_price)
#                 # Update the unit price logic here (e.g., save to database or settings)
#             except ValueError:
#                 pass

#     customers = Customer.objects.all()
#     context = {'customers': customers, 'default_unit_price': default_unit_price}
#     return render(request, 'billing/admin_home.html', context)

def customer_home(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        customer = None

    context = {'customer': customer}
    return render(request, 'billing/customer_home.html', context)

def update_unit_price(request):
    if request.method == 'POST':
        new_unit_price = float(request.POST['unit_price'])
        # Save the new unit price to a session
        request.session['unit_price'] = new_unit_price

    # Redirect back to wherever appropriate
    return redirect('meter_reader_home')

def pay_due_amount(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        # Handle case where customer doesn't exist
        return redirect('customer_home', customer_id=customer_id)

    if request.method == 'POST':
        # Process the payment and update the database
        customer.due_amount = 0
        customer.save()

    return redirect('customer_home', customer_id=customer_id) 


def meter_reader_home(request):
    if request.method == 'POST':
        print("meter reading post ----")
        meter_reading_form = MeterReadingForm(request.POST)
        if meter_reading_form.is_valid():
            meter_reading = meter_reading_form.save()
            customer = meter_reading.customer
            meter_reading_value = meter_reading.meter_reading
            unit_price = 5  # Replace with actual unit price
            customer.due_amount += meter_reading_value * unit_price
            customer.save()

            return redirect('meter_reader_home')
        else:
            print("meter_reading_form.errors=>>", meter_reading_form.errors)
    else:
        meter_reading_form = MeterReadingForm()

    context = {'meter_reading_form': meter_reading_form}
    return render(request, 'billing/meter_reader_home.html', context)

def create_customer(request):
    if request.method == 'POST':
        print("create cutomer post----")
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
          
            return redirect('create_customer')  # Redirect to the same page after creating customer
    else:
        customer_form = CustomerForm()
    return render(request, 'billing/create_customer.html', {'customer_form': customer_form})

def customer_login(request):
    not_found = False  # Initialize the not_found variable
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        try:
            customer = Customer.objects.get(customer_number=customer_id)
            return redirect('customer_home', customer_id=customer.id)
        except Customer.DoesNotExist:
            not_found = True  # Set not_found to True if customer is not found
    
    return render(request, 'billing/customer_login.html', {'not_found': not_found})

def create_invoice(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        amount = float(request.POST.get('amount'))
        customer = Customer.objects.get(pk=customer_id)
        invoice = Invoice(customer=customer, amount=amount)
        invoice.save()
        return redirect('invoice_list')
    customers = Customer.objects.all()
    return render(request, 'billing/create_invoice.html', {'customers': customers})

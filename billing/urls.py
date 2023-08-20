from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer-login/', views.customer_login, name='customer_login'),
    path('customer-home/<int:customer_id>/', views.customer_home, name='customer_home'),
    path('admin/create-customer/', views.create_customer, name='create_customer'),
    path('create-invoice/', views.create_invoice, name='create_invoice'),
    path('meter-reader/', views.meter_reader_home, name='meter_reader_home'),
    path('update_unit_price/', views.update_unit_price, name='update_unit_price'),
    # pay due amount
    path('pay_due_amount/<int:customer_id>/', views.pay_due_amount, name='pay_due_amount'),
    path('meter_reader_home/', views.meter_reader_home, name='meter_reader_home'),
    path('admin-home/', views.admin_home, name='admin_home'),
]

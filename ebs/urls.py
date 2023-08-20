from django.contrib import admin
from django.urls import path, include
from billing import views

urlpatterns = [
    path('', views.home, name='home'),
      path('customer-login/', views.customer_login, name='customer_login'),
    path('customer-home/<int:customer_id>/', views.customer_home, name='customer_home'),
    path('admin/create-customer/', views.create_customer, name='create_customer'),
    path('admin/', admin.site.urls),
    path('billing/', include('billing.urls')),
    path('meter-reader/', views.meter_reader_home, name='meter_reader_home'),
    path('admin-home/', views.admin_home, name='admin_home'),
]

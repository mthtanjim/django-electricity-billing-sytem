# Electricity Billing System

A Django-based web app for electricity billing and customer management.

## Features

- Customer registration and login
- Meter reading submission
- Admin dashboard for customer management
- Billing calculation and payment processing

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Apply database migrations with `python manage.py migrate`.
5. Run the server with `python manage.py runserver`.

## Usage

- Register/login as a customer or meter reader.
- Admins manage customers and set unit prices.
- Customers view due amounts, pay bills, and see billing history.

## Technologies Used

- Django, HTML, CSS
- PostgreSQL (or other production DB)
- Gunicorn, Nginx/Apache (for production)
- AWS/Heroku/Preferred hosting platform

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make changes and submit a pull request.

## Screenshots

### Home Page
![Home](https://github.com/mthtanjim/django-electricity-billing-sytem/blob/master/electricity%20home.png?raw=true)

### Admin Dashboard
![Admin](https://github.com/mthtanjim/django-electricity-billing-sytem/blob/master/admin%20ebs.png?raw=true)

### Meter Reader Page
![Meter Reader](https://github.com/mthtanjim/django-electricity-billing-sytem/blob/master/meter%20reader.png?raw=true)

### Cutoomer Dashboard
![Meter Reader](https://github.com/mthtanjim/django-electricity-billing-sytem/blob/master/customers.png?raw=true)



## License

This project is licensed under the MIT License.

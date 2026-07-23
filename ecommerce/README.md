# E-Commerce Store

A simple and user-friendly Django-based E-Commerce Web Application that allows users to register, log in, browse products, add products to a shopping cart, place orders, and view their order history.

## GitHub Repository

The complete source code of this project is available on GitHub.

**GitHub:**  
https://github.com/fatima-rifa/eco_pro.git

## Live Demo

The deployed E-Commerce Store application is available here.

**Live Demo:**  
https://rifa0.pythonanywhere.com/

## Project Overview

The **E-Commerce Store** is developed using **Python and Django**. The application uses Django's built-in authentication system to manage user registration, login, logout, and sessions.

When users open the website, they first see a landing page with the **E-Commerce Store** name, an image, and **Register** and **Login** buttons.

After successful login, users can access the main e-commerce features such as viewing products, adding products to the cart, buying products, placing orders, viewing order history, and accessing their profile.

Only logged-in users can access the protected features of the application.

## Features

- Landing page for the E-Commerce Store
- User registration
- User login and authentication
- Session-based user management
- User logout
- Protected pages for authenticated users
- Product listing
- Product images
- Add products to cart
- View shopping cart
- Remove products from cart
- Buy Now functionality
- Place individual orders
- View order history
- User profile
- Display logged-in user's name
- Display user's email address
- Display user's phone number
- Django Admin for product management
- Media file handling for product images
- Bootstrap-based responsive user interface

## User Flow

```text
Landing Page
     |
     |-- Register
     |      |
     |      v
     |   Registration Page
     |
     |-- Login
            |
            v
         Home Page
            |
      +-----+------+---------+---------+
      |            |         |         |
      v            v         v         v
   Add to Cart   Buy Now   Profile   Orders
      |            |
      v            v
    Cart       Order Page
      |            |
      |            v
      |       Place Order
      |            |
      |            v
      |        My Orders
      |
      v
    Logout
      |
      v
Landing Page
```

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Django Authentication
- Django Sessions

## Project Structure

```text
ecommerce/
│
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
│
├── ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── shop/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── ...
│   │
│   ├── templates/
│   │   ├── landing.html
│   │   ├── registration.html
│   │   ├── login.html
│   │   ├── home.html
│   │   ├── cart.html
│   │   ├── order.html
│   │   ├── orders.html
│   │   └── profile.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
└── media/
    └── products/
```

## Product Model

The application contains a Product model with the following fields:

- Product Name
- Product Description
- Product Price
- Product Image

Products can be managed through the Django Admin Panel.

## Cart Functionality

Logged-in users can:

1. View products on the home page.
2. Click **Add to Cart** to add a product.
3. Open the cart to view added products.
4. Remove products from the cart.
5. Place an order for individual products.

## Buy Now Functionality

The **Buy Now** button allows users to directly order a product without adding it to the cart.

The user can:

1. Select a product.
2. Click **Buy Now**.
3. View the order page.
4. Select the required quantity.
5. Click **Place Order**.
6. View the order in **My Orders**.

## User Authentication

The application uses Django's built-in authentication system.

Only logged-in users can access:

- Home page
- Add to Cart
- Cart
- Buy Now
- Place Order
- My Orders
- Profile
- Logout

Unauthenticated users cannot access protected e-commerce features.

After logout, the user's session is ended and the user is redirected to the landing page.

## User Profile

The profile page displays:

- Name / Username
- Email
- Phone Number

## Media Files

Product images are uploaded using Django's media file configuration.

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## Static Files

Static files are configured using:

```python
STATIC_URL = 'static/'
```

The project uses Bootstrap through a CDN, and the CSS styles are included directly inside the HTML templates.

## Database

The project uses SQLite as the database during development.

The database contains information related to:

- Users
- Products
- User Profiles
- Carts
- Cart Items
- Orders
- Order Items

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/fatima-rifa/eco_pro.git
```

### 2. Navigate to the Project Folder

```bash
cd eco_pro
```

### 3. Create Virtual Environment

```bash
python -m venv virtual_1
```

### 4. Activate Virtual Environment

On Windows:

```bash
virtual_1\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run Development Server

```bash
python manage.py runserver
```

### 9. Open the Application

Open the following URL in your browser:

```text
http://127.0.0.1:8000/
```

The landing page will be displayed first.

## Django Admin

The Django Admin Panel is used to manage products and other database records.

The admin URL is:

```text
http://127.0.0.1:8000/admin/
```

An administrator can add, edit, update, and delete products from the admin panel.

## Deployment

This project is deployed on **PythonAnywhere**.

The deployment process includes:

- Creating a PythonAnywhere account
- Uploading or cloning the Django project
- Creating a virtual environment
- Installing project dependencies
- Configuring the database
- Running database migrations
- Configuring media files
- Configuring static files
- Setting up WSGI
- Reloading the web application
- Testing the live website

## Live Website

The deployed website can be accessed using the following link:

https://rifa0.pythonanywhere.com/

## Future Improvements

The following features can be added in the future:

- Online payment integration
- Product search
- Product categories
- Product filtering
- Product reviews and ratings
- Order cancellation
- Order status tracking
- Product quantity update in cart
- Email order confirmation
- Improved admin dashboard

## Author

**Fathima Rifa**

## License

This project is created for educational and academic purposes.
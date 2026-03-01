# Flask Ecommerce Mini – Tuckify

Tuckify is a small e-commerce web application built with Flask and connected to a PostgreSQL database. It functions as a simple online store where users can browse products, add them to a shopping cart, and complete the checkout process. This project was created to better understand how e-commerce applications work and to practice building essential features from scratch.

## Features

The application includes a user and administrator authentication system implemented with Flask-Login. It uses a session-based cart system to store selected products and includes checkout logic that creates orders and order items in the database. Administrator routes are protected to prevent unauthorized access and allow full product and order management. The project also includes CSRF protection with Flask-WTF, password hashing using Werkzeug, and secure configuration management through environment variables stored in a .env file.

## Pages

The Shop page displays all available products along with their names, prices, and images, and allows users to add items to their cart. The Cart page shows all selected products, calculates the total price automatically, and provides an option to complete the checkout process. The Login page allows users to authenticate and provides access to registration. The Admin Panel allows administrators to view registered users, manage orders, mark orders as completed, delete orders, and create or update products.

## Tech Stack

The backend of the application is built with Python and Flask. The frontend is developed using HTML, CSS, and JavaScript. PostgreSQL is used as the database system. The project also relies on Flask-Login, Flask-WTF, WTForms, and Werkzeug to handle authentication, form validation, and security.

## Project Goals

The main goal of this project was to strengthen my understanding of Flask architecture and application structure. It was also designed to help me practice authentication and authorization, understand how shopping carts and checkout systems function, and build a working administrative dashboard similar to those used in real online stores.

## Future Improvements

Future improvements may include adding product pagination, implementing unit tests with pytest, creating API endpoints, preparing the application for production deployment, and integrating online payment methods such as PayPal, Visa, or Mastercard.

## Author

This project was created as a personal learning experience focused on improving my Flask development skills and building a practical, real-world style e-commerce application.

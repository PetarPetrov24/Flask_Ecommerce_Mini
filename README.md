# Flask Ecommerce Mini – Tuckify

Tuckify is a small e-commerce web application built with Flask and connected to a PostgreSQL database. It functions as a simple online store where users can browse products, add them to a shopping cart, and complete the checkout process. This project was created to better understand how e-commerce applications work and to practice building essential features from scratch.

## Features

The application includes a user and administrator authentication system implemented with Flask-Login. It uses a session-based cart system to store selected products and includes checkout logic that creates orders and order items in the database. Administrator routes are protected to prevent unauthorized access and allow full product and order management. The project also includes CSRF protection with Flask-WTF, password hashing using Werkzeug, and secure configuration management through environment variables stored in a .env file.

<img width="1916" height="909" alt="image" src="https://github.com/user-attachments/assets/fb653a0f-6482-4582-afd3-f54cf52b10d1" />

After a user is login in:

<img width="1092" height="299" alt="image" src="https://github.com/user-attachments/assets/8129aa26-b1e3-4351-b6cb-9d9629e70b9a" />

After clicking proceed to checkout:

<img width="1093" height="275" alt="image" src="https://github.com/user-attachments/assets/f004be17-62bd-4f7b-9fec-6ae22ed9730b" />



## Pages

The Shop page displays all available products along with their names, prices, and images, and allows users to add items to their cart. The Cart page shows all selected products, calculates the total price automatically, and provides an option to complete the checkout process. The Login page allows users to authenticate and provides access to registration.

<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/dfc64859-c1f0-4ba2-a18d-0a851476719b" />

The Admin Panel allows administrators to view registered users, manage orders, mark orders as completed, delete orders, and create or update products.

<img width="1916" height="905" alt="image" src="https://github.com/user-attachments/assets/a8204fcd-3dad-4476-be0a-0d9ba1308337" />

<img width="1119" height="211" alt="image" src="https://github.com/user-attachments/assets/03962718-6da3-4d13-9f50-3a796ff8ea5b" />







## Tech Stack

The backend of the application is built with Python and Flask. The frontend is developed using HTML, CSS, and JavaScript. PostgreSQL is used as the database system. The project also relies on Flask-Login, Flask-WTF, WTForms, and Werkzeug to handle authentication, form validation, and security.

## Project Goals

The main goal of this project was to strengthen my understanding of Flask architecture and application structure. It was also designed to help me practice authentication and authorization, understand how shopping carts and checkout systems function, and build a working administrative dashboard similar to those used in real online stores.

## Future Improvements

Future improvements may include adding product pagination, implementing unit tests with pytest, creating API endpoints, preparing the application for production deployment, and integrating online payment methods such as PayPal, Visa, or Mastercard.

## Author

This project was created as a personal learning experience focused on improving my Flask development skills and building a practical, real-world style e-commerce application.

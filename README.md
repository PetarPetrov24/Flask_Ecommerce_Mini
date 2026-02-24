Flask Ecommerce Mini – Tuckify

Tuckify is a small e-commerce web app built with Flask and connected to a PostgreSQL database. It works like a simple online shop where users can browse products, add them to a cart, and complete a checkout. I built this project to better understand how real e-commerce applications work and what features are essential behind the scenes.

Pages & Structure

The app has a clean design with a green accent theme, a navigation bar that shows the logged-in user’s nickname, and a simple footer.

The Shop page displays all available products with their name, price, and image, and allows users to add items to their cart.

The Cart page shows everything the user has added, calculates the total price automatically, and provides a checkout option to place the order.

The Login page handles user authentication and includes a link to register a new account.

There’s also an Admin Panel where administrators can view users, manage orders (mark them as completed or delete them), and create or manage products.

Features

The application includes a full authentication system for both users and admins using Flask-Login. Admin routes are protected to prevent unauthorized access. The cart works using session storage, and the checkout process creates orders and order items in the database. Templates are rendered with Jinja2 to dynamically display content.

Security

Security was an important part of this project. Passwords are hashed using Werkzeug Security, sensitive settings are stored in a .env file, CSRF protection is implemented with Flask-WTF, and admin actions require proper authentication.

Tech Stack

The backend is built with Python and Flask, while the frontend uses HTML, CSS, and a bit of JavaScript. PostgreSQL handles the database. The project also uses Flask-Login, Flask-WTF, WTForms, and Werkzeug.

Project Goals

The goal of this project was to get more comfortable with Flask’s structure, practice building authentication and authorization systems, understand how shopping carts and checkout flows work, and create a functional admin dashboard similar to what real online stores use.

Future Improvements

In the future, I’d like to add product pagination, write unit tests with pytest, create API endpoints, prepare the app for production deployment, and integrate real payment methods such as PayPal, Visa, or Mastercard.

Author

This project was created as a personal learning experience to practice Flask and build something close to a real-world e-commerce application.




 

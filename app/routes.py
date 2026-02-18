from flask import render_template, request, redirect, url_for, session, flash, abort
from flask_login import current_user, login_required
from .models import Product, User
from werkzeug.security import check_password_hash, generate_password_hash
from .extensions import db


def register_app(app):
    
    @app.route("/")
    def shop():
        products = Product.query.all()
        return render_template("shop.html", products=products)
    
    @app.route("/add_to_cart/<int:product_id>", methods=["POST"])
    def add_to_cart(product_id):
        quantity = int(request.form.get("quantity", 1))
        cart = session.get("cart", {})
        if product_id in cart:
            card[product_id] += quantity
        else:
            card[product_id] = quantity
        session["cart"] = cart

        flash("Added to cart!")
        return redirect(url_for("shop"))

    @app.route("/login", methods=["GET", "POST"])
    def authentication():
        if request.method == "POST":
            username = request.form["username"] 
            password = request.form["password"]
            user = User.query.filter(username=username).first()
            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for("shop"))
            flash("Invalid credentials")

        return render_template("authentication.html")

    @app.route("/admin")
    @login_required
    def admin():
        if not current_user.is_admin:
            abort(403)
        products = Product.query.all()
        return render_template("admin.html", products=products)
    
    return app
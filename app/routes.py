from flask import render_template, request, redirect, url_for, session, flash, abort
from flask_login import current_user, login_required
from .models import Product, User
from .forms import LoginForm, RegisterForm
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from .extensions import db


def register_app(app):
    
    @app.route("/")
    def intro():
        current_year = datetime.now().year
        return render_template("base.html", current_year=current_year)

    @app.route("/shop")
    def shop():
        page = request.args.get('page', 1, type=int)
        per_page = 10

        pagination = Product.query.paginate(page=page, per_page=per_page, error_out=False)
        products = pagination.items

        has_next = pagination.has_next
        has_prev = pagination.has_prev

        return render_template(
            "shop.html",
            products=products,
            page=page,
            has_next=has_next,
            has_prev=has_prev
        )
    
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
        form = LoginForm()
        if form.validate_on_submit():
            username = request.form["username"] 
            password = request.form["password"]
            user = User.query.filter(username=username).first()
            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for("shop"))
            flash("Invalid credentials")

        return render_template("authentication.html", form=form)
    
    @app.route("/register", methods=["GET", "POST"])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            username = request.form.get("username")
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_passowrd")

            if password != confirm_passowrd:
                flash("Passwords do not match")
                return redirect(url_for("register"))

            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()

            flash("Account created successfully!")
            return redirect(url_for("authentication"))

        return render_template("register.html", form=form)

    @app.route("/admin")
    @login_required
    def admin():
        if not current_user.is_admin:
            abort(403)
        products = Product.query.all()
        total_users = User.query.count()
        total_orders = Order.query.count()
        completed_sales_count = Order.query.filter_by(status=True).count
        pending_orders = Order.query.filter_by(status=False).count()
        total_sales = db.session.query(db.func.sum(Order.total_price)).scalar() or 0
        return render_template(
            "admin.html",
            products=products,
            total_users=total_users,
            total_orders=total_orders,
            completed_sales_count=completed_sales_count,
            pending_orders=pending_orders,
            total_sales=total_sales)
    
    return app
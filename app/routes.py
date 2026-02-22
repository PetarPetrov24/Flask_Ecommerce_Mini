import os
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, session, flash, abort
from flask_login import current_user, login_required, login_user, logout_user
from .models import Product, User, Order
from .forms import LoginForm, RegisterForm, AddProduct, RemoveFromCartForm
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from .extensions import db

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def register_app(app):
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'images', 'products')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    @app.route("/admin/add_product", methods=["GET", "POST"])
    @login_required
    def add_product():
        if not current_user.is_admin:
            flash("Access denied!", "danger")
            return redirect(url_for("shop"))

        form = AddProduct()
        if form.validate_on_submit():
            filename = None
            if form.image.data:  
                image_file = form.image.data
                filename = secure_filename(image_file.filename)

                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
              
                image_file.save(file_path) 

            product = Product(
                name=form.name.data,
                description=form.description.data,
                price=form.price.data,
                stock=form.stock.data,
                image_filename=filename
            )
            db.session.add(product)
            db.session.commit()
            flash("Product added successfully!", "success")
            return redirect(url_for("admin"))

        return render_template("add_product.html", form=form)
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
        product_id = str(product_id)

        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        session["cart"] = cart

        flash("Added to cart!")
        return redirect(url_for("shop"))

    @app.route("/cart")
    def cart():
        cart = session.get('cart', {})
        products = []
        total = 0

        for pid, qty in cart.items():
            product = Product.query.get(pid)
            if product:
                subtotal = product.price * qty
                total += subtotal
                products.append({'product': product, 'quantity': qty, 'subtotal': subtotal})

        return render_template("cart.html", products=products, total=total, remove_form=RemoveFromCartForm())


    @app.route("/remove_from_cart/<int:product_id>", methods=["POST"])
    def remove_from_cart(product_id):
        # Get the current cart from session
        cart = session.get('cart', {})
        product_id_str = str(product_id)

        # Remove the item if it exists
        if product_id_str in cart:
            del cart[product_id_str]

        # If the cart is now empty, remove it completely from session
        if not cart:
            session.pop('cart', None)
        else:
            # Otherwise, update the session cart
            session['cart'] = cart

        session.modified = True  # mark session as changed
        return redirect(url_for('cart'))

    @app.route("/checkout", methods=["POST"])
    @login_required
    def checkout():
        cart = session.get("cart", {})

        if not cart:
            flash("Cart is empty!", "danger")
            return redirect(url_for('shop'))
        total_price = 0

        for product_id, quantity in cart.items():
            product = Product.query.get(int(product_id))
            if product:
                total_price += product.price * quantity

        order = Order(user_id=current_user.id, total_price=total_price, status=True)
        db.session.add(order)
        db.session.commit()

        session["cart"] = {}

        flash("Order placed successfully!", "success")
        return redirect(url_for("shop"))
    
    @app.route("/api/products")
    def api_products():
        products = Product.query.all()
        return jsonify([{
        "id": p.id,
        "name": p.name,
        "price": float(p.price),
        "stock": p.stock,
        "description": p.description
        } for p in products])

    @app.route("/login", methods=["GET", "POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                login_user(user)

                if getattr(user, "is_admin", False):
                    return redirect(url_for("admin"))
                
                return redirect(url_for("shop"))
            flash("Invalid credentials", "danger")

        return render_template("authentication.html", form=form)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("shop"))
    
    @app.route("/register", methods=["GET", "POST"])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            confirm_password = form.confirm_password.data

            if password != confirm_password:
                flash("Passwords do not match")
                return redirect(url_for("register"))

            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("login"))

        return render_template("register.html", form=form)

    @app.route("/admin")
    @login_required
    def admin():
        if not current_user.is_admin:
            abort(403)
        products = Product.query.all()
        total_users = User.query.count()
        total_orders = Order.query.count()
        completed_sales_count = Order.query.filter_by(status=True).count()
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

    @app.route("/admin/users")
    @login_required
    def admin_users():
        if not current_user.is_admin:
            abort(403)  

        users = User.query.all() 
        return render_template("admin_users.html", users=users)

    @app.route("/admin/orders")
    @login_required
    def admin_orders():
        if not current_user.is_admin:
            abort(403)  

        orders = Order.query.all() 
        return render_template("admin_orders.html", orders=orders)

    return app

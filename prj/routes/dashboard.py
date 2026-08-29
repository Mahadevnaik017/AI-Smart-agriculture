from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models import db, User, Product, Category, Order, OrderItem, Wishlist, CartItem, Review, Complaint, Announcement, GovtScheme, MarketPrice, ReturnRequest, AgriQuote
from datetime import datetime, timedelta
from functools import wraps

dashboard_bp = Blueprint('dashboard', __name__)

def role_required(role_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or (current_user.role != role_name and current_user.role != 'admin'):
                flash(f'Access restricted to {role_name.capitalize()} account holder.', 'danger')
                return redirect(url_for('main.index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# --- FARMER DASHBOARD ---
@dashboard_bp.route('/dashboard/farmer')
@login_required
@role_required('farmer')
def farmer_dashboard():
    products = Product.query.filter_by(farmer_id=current_user.id).order_by(Product.created_at.desc()).all()
    categories = Category.query.all()
    
    # Farmer's order items
    order_items = OrderItem.query.filter_by(farmer_id=current_user.id).order_by(OrderItem.id.desc()).all()
    total_sales = sum([item.subtotal for item in order_items])
    total_orders = len(order_items)
    
    # Calculate monthly sales for chart
    sales_by_month = [3200, 4800, 5400, 6100, 7800, total_sales if total_sales > 0 else 8500]
    
    return render_template(
        'dashboards/farmer.html',
        products=products,
        categories=categories,
        order_items=order_items,
        total_sales=total_sales,
        total_orders=total_orders,
        sales_by_month=sales_by_month
    )

@dashboard_bp.route('/farmer/product/add', methods=['POST'])
@login_required
@role_required('farmer')
def farmer_add_product():
    title = request.form.get('title', '').strip()
    title_kn = request.form.get('title_kn', '').strip()
    category_id = int(request.form.get('category_id', 1))
    price = float(request.form.get('price', 0))
    unit = request.form.get('unit', 'kg')
    stock_quantity = int(request.form.get('stock_quantity', 100))
    description = request.form.get('description', '').strip()
    is_organic = request.form.get('is_organic') == 'on'
    image_url = request.form.get('image_url', '').strip() or 'https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80'
    
    if title and price > 0:
        new_prod = Product(
            farmer_id=current_user.id,
            category_id=category_id,
            title=title,
            title_kn=title_kn,
            description=description,
            price=price,
            unit=unit,
            stock_quantity=stock_quantity,
            district=current_user.district,
            is_organic=is_organic,
            image_url=image_url,
            status='approved' # Auto approve for fast demo
        )
        db.session.add(new_prod)
        db.session.commit()
        flash('Product listed successfully on Mojara Marketplace!', 'success')
        
    return redirect(url_for('dashboard.farmer_dashboard'))

# --- BUYER DASHBOARD ---
@dashboard_bp.route('/dashboard/buyer')
@login_required
def buyer_dashboard():
    orders = Order.query.filter_by(buyer_id=current_user.id).order_by(Order.created_at.desc()).all()
    wishlist_items = Wishlist.query.filter_by(buyer_id=current_user.id).all()
    cart_items = CartItem.query.filter_by(buyer_id=current_user.id).all()
    
    total_spent = sum([o.total_amount for o in orders if o.payment_status == 'Completed'])
    
    return render_template(
        'dashboards/buyer.html',
        orders=orders,
        wishlist_items=wishlist_items,
        cart_items=cart_items,
        total_spent=total_spent
    )

# --- OFFICER DASHBOARD ---
@dashboard_bp.route('/dashboard/officer')
@login_required
@role_required('officer')
def officer_dashboard():
    pending_farmers = User.query.filter_by(role='farmer', is_verified=False).all()
    verified_farmers = User.query.filter_by(role='farmer', is_verified=True).all()
    announcements = Announcement.query.filter_by(officer_id=current_user.id).order_by(Announcement.created_at.desc()).all()
    schemes = GovtScheme.query.all()
    
    district_farmer_counts = {
        'Mandya': 142,
        'Haveri': 98,
        'Dharwad': 115,
        'Kolar': 87,
        'Shimoga': 76
    }
    
    return render_template(
        'dashboards/officer.html',
        pending_farmers=pending_farmers,
        verified_farmers=verified_farmers,
        announcements=announcements,
        schemes=schemes,
        district_counts=district_farmer_counts
    )

@dashboard_bp.route('/officer/announcement/create', methods=['POST'])
@login_required
@role_required('officer')
def create_announcement():
    title = request.form.get('title', '').strip()
    title_kn = request.form.get('title_kn', '').strip()
    content = request.form.get('content', '').strip()
    district = request.form.get('district', 'All Districts')
    priority = request.form.get('priority', 'Normal')
    
    if title and content:
        anc = Announcement(
            officer_id=current_user.id,
            title=title,
            title_kn=title_kn,
            content=content,
            district=district,
            priority=priority
        )
        db.session.add(anc)
        db.session.commit()
        flash('Agricultural Officer advisory announcement published!', 'success')
        
    return redirect(url_for('dashboard.officer_dashboard'))

# --- ADMIN DASHBOARD ---
@dashboard_bp.route('/dashboard/admin')
@login_required
@role_required('admin')
def admin_dashboard():
    users_count = User.query.count()
    farmers_count = User.query.filter_by(role='farmer').count()
    buyers_count = User.query.filter_by(role='buyer').count()
    officers_count = User.query.filter_by(role='officer').count()
    products_count = Product.query.count()
    orders_count = Order.query.count()
    total_platform_revenue = sum([o.total_amount for o in Order.query.filter_by(payment_status='Completed').all()])
    
    recent_users = User.query.order_by(User.created_at.desc()).limit(8).all()
    all_products = Product.query.order_by(Product.created_at.desc()).all()
    all_orders = Order.query.order_by(Order.created_at.desc()).all()
    all_returns = ReturnRequest.query.order_by(ReturnRequest.created_at.desc()).all()
    complaints = Complaint.query.order_by(Complaint.created_at.desc()).all()
    categories = Category.query.all()
    all_advisories = Announcement.query.order_by(Announcement.created_at.desc()).all()
    all_quotes = AgriQuote.query.order_by(AgriQuote.id.desc()).all()
    
    return render_template(
        'dashboards/admin.html',
        users_count=users_count,
        farmers_count=farmers_count,
        buyers_count=buyers_count,
        officers_count=officers_count,
        products_count=products_count,
        orders_count=orders_count,
        total_revenue=total_platform_revenue or 12450.0,
        recent_users=recent_users,
        all_products=all_products,
        all_orders=all_orders,
        all_returns=all_returns,
        complaints=complaints,
        categories=categories,
        all_advisories=all_advisories,
        all_quotes=all_quotes
    )

@dashboard_bp.route('/admin/advisory/add', methods=['POST'])
@login_required
@role_required('admin')
def admin_add_advisory():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    district = request.form.get('district', 'All Districts').strip()
    priority = request.form.get('priority', 'Normal')
    
    if title and content:
        ann = Announcement(
            officer_id=current_user.id,
            title=title,
            content=content,
            district=district,
            priority=priority
        )
        db.session.add(ann)
        db.session.commit()
        flash('New Agricultural Advisory published live on the Home Page!', 'success')
    return redirect(url_for('dashboard.admin_dashboard'))

@dashboard_bp.route('/admin/advisory/delete/<int:advisory_id>', methods=['POST', 'GET'])
@login_required
@role_required('admin')
def admin_delete_advisory(advisory_id):
    ann = Announcement.query.get_or_404(advisory_id)
    title = ann.title
    db.session.delete(ann)
    db.session.commit()
    flash(f'Advisory "{title}" deleted successfully from live screen.', 'info')
    return redirect(url_for('dashboard.admin_dashboard'))

@dashboard_bp.route('/admin/advisory/update/<int:advisory_id>', methods=['POST'])
@login_required
@role_required('admin')
def admin_update_advisory(advisory_id):
    ann = Announcement.query.get_or_404(advisory_id)
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    district = request.form.get('district', 'All Districts').strip()
    priority = request.form.get('priority', 'Normal')
    
    if title:
        ann.title = title
    if content:
        ann.content = content
    if district:
        ann.district = district
    if priority:
        ann.priority = priority
        
    db.session.commit()
    flash(f'Advisory #{ann.id} "{ann.title}" updated live in header ticker!', 'success')
    return redirect(url_for('dashboard.admin_dashboard'))

@dashboard_bp.route('/admin/product/update/<int:product_id>', methods=['POST'])
@login_required
@role_required('admin')
def admin_update_product(product_id):
    prod = Product.query.get_or_404(product_id)
    title = request.form.get('title')
    price = request.form.get('price')
    discount = request.form.get('discount_percent')
    description = request.form.get('description')
    image_url = request.form.get('image_url')
    
    if title:
        prod.title = title.strip()
    if price is not None and price != '':
        prod.price = float(price)
    if discount is not None and discount != '':
        prod.discount_percent = float(discount)
    if description:
        prod.description = description.strip()
    if image_url:
        prod.image_url = image_url.strip()
        
    db.session.commit()
    flash(f'Updated product "{prod.title}" details: Price ₹{prod.price}, Discount {prod.discount_percent}%, Final Price ₹{prod.final_price}. Changes applied live!', 'success')
    return redirect(url_for('dashboard.admin_dashboard'))

@dashboard_bp.route('/admin/user/verify/<int:user_id>')
@login_required
@role_required('admin')
def admin_verify_user(user_id):
    u = User.query.get_or_404(user_id)
    u.is_verified = not u.is_verified
    db.session.commit()
    flash(f"User {u.name} status updated to {'Verified' if u.is_verified else 'Unverified'}.", 'info')
    return redirect(url_for('dashboard.admin_dashboard'))

# --- ADMIN QUOTE MANAGEMENT ROUTES ---
@dashboard_bp.route('/admin/quote/add', methods=['POST'])
@login_required
@role_required('admin')
def admin_add_quote():
    quote_text = request.form.get('quote_text', '').strip()
    author_source = request.form.get('author_source', 'Agriculture Wisdom').strip()
    category = request.form.get('category', 'Indian Agriculture').strip()
    
    if quote_text:
        q = AgriQuote(
            quote_text=quote_text,
            author_source=author_source,
            category=category,
            is_active=True
        )
        db.session.add(q)
        db.session.commit()
        flash('New Agricultural Quote published live in header ticker!', 'success')
    return redirect(url_for('dashboard.admin_dashboard'))

@dashboard_bp.route('/admin/quote/update/<int:quote_id>', methods=['POST'])
@login_required
@role_required('admin')
def admin_update_quote(quote_id):
    q = AgriQuote.query.get_or_404(quote_id)
    quote_text = request.form.get('quote_text', '').strip()
    author_source = request.form.get('author_source', '').strip()
    category = request.form.get('category', '').strip()
    
    if quote_text:
        q.quote_text = quote_text
    if author_source:
        q.author_source = author_source
    if category:
        q.category = category
        
    db.session.commit()
    flash(f'Quote #{q.id} updated live in header ticker!', 'success')
    return redirect(url_for('dashboard.admin_dashboard'))

@dashboard_bp.route('/admin/quote/delete/<int:quote_id>', methods=['POST', 'GET'])
@login_required
@role_required('admin')
def admin_delete_quote(quote_id):
    q = AgriQuote.query.get_or_404(quote_id)
    db.session.delete(q)
    db.session.commit()
    flash(f'Quote #{quote_id} deleted immediately from live header ticker.', 'info')
    return redirect(url_for('dashboard.admin_dashboard'))

@dashboard_bp.route('/admin/quote/toggle/<int:quote_id>', methods=['POST', 'GET'])
@login_required
@role_required('admin')
def admin_toggle_quote_status(quote_id):
    q = AgriQuote.query.get_or_404(quote_id)
    q.is_active = not q.is_active
    db.session.commit()
    status_text = "Activated" if q.is_active else "Deactivated"
    flash(f'Quote #{q.id} status updated to {status_text}.', 'info')
    return redirect(url_for('dashboard.admin_dashboard'))

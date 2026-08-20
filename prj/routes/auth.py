# ========================================================================================
# AI-Driven Smart Agriculture & Micro-crop Advisory System (Mojara)
# Module: User Authentication & Profile Routing Controller (routes/auth.py)
# Assigned Engineer: Kiran Muttappa Andani
# Milestone: User registration backend and password hashing with PBKDF2 (17 August 2026)
# ========================================================================================
# Session Management & Role Redirection:
# Handles authenticated sessions via Flask-Login and routes users to role-specific dashboards.
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
@auth_bp.route('/login/', methods=['GET', 'POST'], strict_slashes=False)
@auth_bp.route('/signin', methods=['GET', 'POST'], strict_slashes=False)
@auth_bp.route('/auth/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if current_user.is_authenticated:
        return redirect_role_dashboard(current_user)
        
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            flash('Invalid email or password. Please try again.', 'danger')
            return render_template('auth/login.html')
            
        login_user(user, remember=remember)
        flash(f'Welcome back, {user.name}!', 'success')
        
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        return redirect_role_dashboard(user)
        
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'], strict_slashes=False)
@auth_bp.route('/register/', methods=['GET', 'POST'], strict_slashes=False)
@auth_bp.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
@auth_bp.route('/auth/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if current_user.is_authenticated:
        return redirect_role_dashboard(current_user)
        
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        role = request.form.get('role', 'buyer')
        phone = request.form.get('phone', '').strip()
        district = request.form.get('district', 'Bengaluru Urban')
        address = request.form.get('address', '').strip()
        
        existing = User.query.filter_by(email=email).first()
        if existing:
            flash('An account with this email already exists.', 'warning')
            return render_template('auth/register.html')
            
        new_user = User(
            name=name,
            email=email,
            role=role,
            phone=phone,
            district=district,
            address=address,
            is_verified=True if role == 'buyer' else True # Auto verify for demo
        )
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user, remember=True)
        flash('Account created successfully! Welcome to your Mojara Dashboard.', 'success')
        return redirect_role_dashboard(new_user)
        
    return render_template('auth/register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.name = request.form.get('name', current_user.name).strip()
        current_user.phone = request.form.get('phone', current_user.phone).strip()
        current_user.district = request.form.get('district', current_user.district)
        current_user.address = request.form.get('address', current_user.address).strip()
        
        new_pw = request.form.get('new_password', '').strip()
        if new_pw:
            current_user.set_password(new_pw)
            
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('auth.profile'))
        
    return render_template('auth/profile.html')

def redirect_role_dashboard(user):
    if user.role == 'farmer':
        return redirect(url_for('dashboard.farmer_dashboard'))
    elif user.role == 'officer':
        return redirect(url_for('dashboard.officer_dashboard'))
    elif user.role == 'admin':
        return redirect(url_for('dashboard.admin_dashboard'))
    else:
        return redirect(url_for('dashboard.buyer_dashboard'))

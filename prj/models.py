# ========================================================================================
# AI-Driven Smart Agriculture & Micro-crop Advisory System (Mojara)
# Module: Relational Database Models & SQLAlchemy Schema (models.py)
# Assigned Engineer: Kiran Muttappa Andani
# Milestone: Data storage requirements review for agriculture platform (25 July 2026)
# ========================================================================================
# Relational Database Architecture:
# Supports Users, Products, Orders, MarketPrices, Announcements, and AI Logs.
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='buyer') # farmer, buyer, officer, admin
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.Text, nullable=True)
    district = db.Column(db.String(100), nullable=False, default='Bengaluru Rural')
    state = db.Column(db.String(100), nullable=False, default='Karnataka')
    is_verified = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    products = db.relationship('Product', backref='farmer', lazy=True, foreign_keys='Product.farmer_id')
    orders = db.relationship('Order', backref='buyer', lazy=True, foreign_keys='Order.buyer_id')
    forum_posts = db.relationship('ForumPost', backref='author', lazy=True)
    reviews = db.relationship('Review', backref='author', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'phone': self.phone,
            'district': self.district,
            'state': self.state,
            'is_verified': self.is_verified,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M')
        }

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    name_kn = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(50), default='fa-leaf')
    
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    title_kn = db.Column(db.String(150), nullable=True)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    discount_percent = db.Column(db.Float, default=0.0) # Admin discount percentage
    unit = db.Column(db.String(20), default='kg') # kg, ton, quintal, bag
    stock_quantity = db.Column(db.Integer, default=100)
    district = db.Column(db.String(100), nullable=False, default='Bengaluru Rural')
    is_organic = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(255), default='/static/images/products/default.jpg')
    status = db.Column(db.String(20), default='approved') # pending, approved, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    reviews = db.relationship('Review', backref='product', lazy=True, cascade='all, delete-orphan')

    @property
    def display_image_url(self):
        title_lower = (self.title or '').lower()
        if 'cotton' in title_lower or 'bt cotton' in title_lower:
            return '/static/images/crops/bt_cotton_seeds.jpg'
        elif 'ragi' in title_lower or 'finger millet' in title_lower:
            return '/static/images/crops/ragi.jpg'
        elif 'tomato' in title_lower or 'tomatoes' in title_lower:
            return '/static/images/crops/tomatoes.jpg'
        elif 'rice' in title_lower or 'paddy' in title_lower or 'masoori' in title_lower:
            return '/static/images/crops/rice.jpg'
        elif 'vermicompost' in title_lower or 'compost' in title_lower or 'fertilizer' in title_lower:
            return '/static/images/crops/vermicompost.jpg'
        elif 'sprayer' in title_lower or 'knapsack' in title_lower or 'tool' in title_lower:
            return '/static/images/crops/sprayer.jpg'
        elif 'neem' in title_lower or 'pesticide' in title_lower:
            return '/static/images/crops/neem_oil.jpg'
        
        if self.image_url and not self.image_url.startswith('https://images.unsplash.com'):
            return self.image_url
            
        return '/static/images/crops/default.jpg'

    @property
    def final_price(self):
        if self.discount_percent and self.discount_percent > 0:
            return round(self.price * (1.0 - (self.discount_percent / 100.0)), 2)
        return self.price

    @property
    def average_rating(self):
        if not self.reviews:
            return 4.5
        return round(sum([r.rating for r in self.reviews]) / len(self.reviews), 1)

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    product = db.relationship('Product', lazy=True)

class Wishlist(db.Model):
    __tablename__ = 'wishlists'
    
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    product = db.relationship('Product', lazy=True)

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    buyer_name = db.Column(db.String(100), nullable=True)
    buyer_email = db.Column(db.String(120), nullable=True)
    buyer_phone = db.Column(db.String(20), nullable=True)
    total_amount = db.Column(db.Float, nullable=False)
    shipping_address = db.Column(db.Text, nullable=False)
    payment_method = db.Column(db.String(50), default='UPI') # UPI, COD
    payment_status = db.Column(db.String(20), default='Completed') # Pending, Completed, Failed, Refunded
    order_status = db.Column(db.String(30), default='Processing') # Processing, Shipped, Out for Delivery, Delivered, Return Requested, Refunded
    upi_utr = db.Column(db.String(100), nullable=True) # UPI Transaction Reference UTR
    tracking_stage = db.Column(db.Integer, default=1) # 1: Placed, 2: Harvested & Packed, 3: In Transit, 4: Delivered
    tracking_location = db.Column(db.String(150), default='Mandya Quality Control Hub')
    estimated_delivery = db.Column(db.String(50), default='Within 2 Business Days')
    is_return_requested = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')
    return_request = db.relationship('ReturnRequest', backref='order', uselist=False, lazy=True, cascade='all, delete-orphan')

    @property
    def current_stage(self):
        if self.tracking_stage and self.tracking_stage > 1:
            return self.tracking_stage
        if not self.created_at:
            return 1
        elapsed = datetime.utcnow() - self.created_at
        hours = elapsed.total_seconds() / 3600.0
        if hours < 24:
            return 1 # Day 1: Order Placed & Verified
        elif hours < 48:
            return 2 # Day 2: Harvested & Quality Packed
        elif hours < 72:
            return 3 # Day 3: In Transit
        else:
            return 4 # Day 4: Delivered

    @property
    def current_location(self):
        if self.tracking_location and self.tracking_location != 'Mandya Quality Control Hub':
            return self.tracking_location
        stage = self.current_stage
        if stage == 1:
            return 'Mandya Agro Quality Control & Direct Farmer Hub'
        elif stage == 2:
            return 'Bengaluru Central Sorting & Cold Storage Center'
        elif stage == 3:
            return 'In Transit via Express Fleet Vehicle #KA-05-AG-4921'
        else:
            return 'Delivered to Customer Doorstep Address'

    @property
    def current_status(self):
        if self.order_status in ['Return Requested', 'Refunded']:
            return self.order_status
        stage = self.current_stage
        if stage == 1:
            return 'Processing & Verified'
        elif stage == 2:
            return 'Harvested & Packed'
        elif stage == 3:
            return 'Out for Delivery'
        else:
            return 'Delivered'

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
    
    product = db.relationship('Product', lazy=True)
    farmer = db.relationship('User', lazy=True, foreign_keys=[farmer_id])

class ReturnRequest(db.Model):
    __tablename__ = 'return_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    refund_status = db.Column(db.String(50), default='Pending Pickup') # Pending Pickup, Item Received & Verified, Refund Completed
    refund_amount = db.Column(db.Float, nullable=False)
    refund_method = db.Column(db.String(100), default='UPI Auto Refund (1-2 Days)') # UPI Auto Refund or On-the-Spot Cash Refund
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    buyer = db.relationship('User', lazy=True)

class CropRecommendationLog(db.Model):
    __tablename__ = 'crop_recommendations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    soil_type = db.Column(db.String(50), nullable=False)
    ph = db.Column(db.Float, nullable=False)
    nitrogen = db.Column(db.Float, nullable=False)
    phosphorus = db.Column(db.Float, nullable=False)
    potassium = db.Column(db.Float, nullable=False)
    rainfall = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    season = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    recommended_crop = db.Column(db.String(100), nullable=False)
    recommended_crop_kn = db.Column(db.String(100), nullable=True)
    expected_yield = db.Column(db.String(50), nullable=False)
    profit_estimate = db.Column(db.String(50), nullable=False)
    guidance = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class DiseaseDetectionLog(db.Model):
    __tablename__ = 'disease_detections'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    crop_name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    detected_disease = db.Column(db.String(150), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    prevention = db.Column(db.Text, nullable=False)
    treatment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class MarketPrice(db.Model):
    __tablename__ = 'market_prices'
    
    id = db.Column(db.Integer, primary_key=True)
    commodity = db.Column(db.String(100), nullable=False)
    commodity_kn = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    mandi_name = db.Column(db.String(100), nullable=False)
    min_price = db.Column(db.Float, nullable=False)
    max_price = db.Column(db.Float, nullable=False)
    modal_price = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), default='Quintal')
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)

class GovtScheme(db.Model):
    __tablename__ = 'govt_schemes'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    title_kn = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    description_kn = db.Column(db.Text, nullable=True)
    eligibility = db.Column(db.Text, nullable=False)
    benefit_amount = db.Column(db.String(100), nullable=False)
    apply_link = db.Column(db.String(255), default='#')
    officer_contact = db.Column(db.String(100), nullable=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

class Announcement(db.Model):
    __tablename__ = 'announcements'
    
    id = db.Column(db.Integer, primary_key=True)
    officer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    title_kn = db.Column(db.String(200), nullable=True)
    content = db.Column(db.Text, nullable=False)
    district = db.Column(db.String(100), default='All Districts')
    priority = db.Column(db.String(20), default='Normal') # Normal, High, Urgent
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    officer = db.relationship('User', lazy=True)

class ForumPost(db.Model):
    __tablename__ = 'forum_posts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), default='General')
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    comments = db.relationship('ForumComment', backref='post', lazy=True, cascade='all, delete-orphan')

class ForumComment(db.Model):
    __tablename__ = 'forum_comments'
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('forum_posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    is_officer_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', lazy=True)

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=5)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Complaint(db.Model):
    __tablename__ = 'complaints'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), default='Open') # Open, In Progress, Resolved
    resolution_notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', lazy=True)

class Advertisement(db.Model):
    __tablename__ = 'advertisements'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    target_url = db.Column(db.String(255), default='#')
    location_banner = db.Column(db.String(50), default='home_top')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class AgriQuote(db.Model):
    __tablename__ = 'agri_quotes'
    
    id = db.Column(db.Integer, primary_key=True)
    quote_text = db.Column(db.Text, nullable=False)
    author_source = db.Column(db.String(150), default='Agriculture Wisdom')
    category = db.Column(db.String(50), default='Indian Agriculture')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

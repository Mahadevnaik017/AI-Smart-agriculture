from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import current_user, login_required
from models import db, Product, Category, MarketPrice, GovtScheme, Announcement, ForumPost, ForumComment, Review, CartItem, Wishlist, Order, OrderItem, Advertisement, ReturnRequest
from ai_engine import predict_crop, recommend_fertilizer, detect_disease
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    featured_products = Product.query.filter_by(status='approved').order_by(Product.created_at.desc()).limit(6).all()
    categories = Category.query.all()
    recent_prices = MarketPrice.query.order_by(MarketPrice.date_updated.desc()).limit(5).all()
    schemes = GovtScheme.query.limit(3).all()
    announcements = Announcement.query.order_by(Announcement.created_at.desc()).limit(3).all()
    ads = Advertisement.query.filter_by(is_active=True).all()
    
    return render_template(
        'index.html',
        featured_products=featured_products,
        categories=categories,
        recent_prices=recent_prices,
        schemes=schemes,
        announcements=announcements,
        ads=ads
    )

@main_bp.route('/marketplace')
def marketplace():
    category_id = request.args.get('category', type=int)
    search_query = request.args.get('q', '').strip()
    district_filter = request.args.get('district', '').strip()
    organic_only = request.args.get('organic') == 'true'
    sort_by = request.args.get('sort', 'newest')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    in_stock_only = request.args.get('in_stock') == 'true'
    min_rating = request.args.get('min_rating', type=float)
    
    query = Product.query.filter_by(status='approved')
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    if search_query:
        query = query.filter((Product.title.ilike(f'%{search_query}%')) | (Product.description.ilike(f'%{search_query}%')))
    if district_filter:
        query = query.filter(Product.district.ilike(f'%{district_filter}%'))
    if organic_only:
        query = query.filter_by(is_organic=True)
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    if in_stock_only:
        query = query.filter(Product.stock_quantity > 0)
    if min_rating is not None:
        query = query.filter(Product.average_rating >= min_rating)
        
    if sort_by == 'price_low':
        query = query.order_by(Product.price.asc())
    elif sort_by == 'price_high':
        query = query.order_by(Product.price.desc())
    elif sort_by == 'rating_high':
        query = query.order_by(Product.average_rating.desc())
    else:
        query = query.order_by(Product.created_at.desc())
        
    products = query.all()
    categories = Category.query.all()
    districts = db.session.query(Product.district).distinct().all()
    districts = [d[0] for d in districts if d[0]]
    
    # Fallback recommendations if searched item does not exist
    recommended_products = []
    is_fallback = False
    if len(products) == 0 and search_query:
        is_fallback = True
        recommended_products = Product.query.filter_by(status='approved').order_by(Product.created_at.desc()).limit(6).all()
    
    return render_template(
        'marketplace.html',
        products=products,
        categories=categories,
        districts=districts,
        selected_category=category_id,
        search_query=search_query,
        district_filter=district_filter,
        organic_only=organic_only,
        sort_by=sort_by,
        min_price=min_price,
        max_price=max_price,
        in_stock_only=in_stock_only,
        min_rating=min_rating,
        is_fallback=is_fallback,
        recommended_products=recommended_products
    )

@main_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    related_products = Product.query.filter(Product.category_id == product.category_id, Product.id != product.id).limit(4).all()
    reviews = Review.query.filter_by(product_id=product.id).order_by(Review.created_at.desc()).all()
    
    is_in_wishlist = False
    if current_user.is_authenticated:
        w = Wishlist.query.filter_by(buyer_id=current_user.id, product_id=product.id).first()
        if w:
            is_in_wishlist = True
            
    return render_template(
        'product_detail.html',
        product=product,
        related_products=related_products,
        reviews=reviews,
        is_in_wishlist=is_in_wishlist
    )

# --- ORDER CONFIRMATION PAGE ---
@main_bp.route('/order/confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    if order.buyer_id != current_user.id and current_user.role != 'admin':
        flash('Unauthorized access to order confirmation.', 'danger')
        return redirect(url_for('main.index'))
        
    return render_template('order_confirmation.html', order=order)

# --- LIVE ORDER TRACKING PAGE ---
@main_bp.route('/order/track/<int:order_id>')
@login_required
def order_tracking(order_id):
    order = Order.query.get_or_404(order_id)
    if order.buyer_id != current_user.id and current_user.role != 'admin' and current_user.role != 'officer':
        flash('Unauthorized access to order tracking.', 'danger')
        return redirect(url_for('main.index'))
        
    return render_template('order_track.html', order=order)

@main_bp.route('/ai/crop-recommendation', methods=['GET', 'POST'])
def ai_crop():
    prediction = None
    if request.method == 'POST':
        state = request.form.get('state', '').strip()
        district = request.form.get('district', '').strip()
        taluk = request.form.get('taluk', '').strip()
        village = request.form.get('village', '').strip()
        
        soil_type = request.form.get('soil_type', 'Red Loam')
        ph = float(request.form.get('ph', 7.0))
        n = float(request.form.get('nitrogen', 40))
        p = float(request.form.get('phosphorus', 30))
        k = float(request.form.get('potassium', 30))
        rainfall = float(request.form.get('rainfall', 650))
        humidity = float(request.form.get('humidity', 65))
        temp = float(request.form.get('temperature', 27))
        season = request.form.get('season', 'Kharif')
        water_avail = request.form.get('water_avail', 'Medium')

        from location_data import get_agri_baseline_by_hierarchy, get_major_crops_for_location
        baseline, data_level_badge = get_agri_baseline_by_hierarchy(state, district, taluk, village)

        # Location hierarchy verification
        loc_display = f"{village}, {taluk}, {district}, {state}" if (village and taluk and district) else (district or "Karnataka")
        
        prediction = predict_crop(soil_type, ph, n, p, k, rainfall, humidity, temp, season, loc_display, water_avail)
        if prediction:
            prediction['location_hierarchy'] = {
                'state': state,
                'district': district,
                'taluk': taluk,
                'village': village,
                'data_level_badge': data_level_badge
            }

    # Look up major crops for the selected location (GET or POST)
    village_q = request.form.get('village', '').strip() if request.method == 'POST' else ''
    taluk_q = request.form.get('taluk', '').strip() if request.method == 'POST' else ''
    district_q = request.form.get('district', '').strip() if request.method == 'POST' else ''
    from location_data import get_major_crops_for_location
    major_crops, major_crops_location, major_crops_source = get_major_crops_for_location(
        village=village_q, taluk=taluk_q, district=district_q
    )

    return render_template('ai_crop.html', prediction=prediction,
                           major_crops=major_crops,
                           major_crops_location=major_crops_location,
                           major_crops_source=major_crops_source)

@main_bp.route('/ai/fertilizer-recommendation', methods=['GET', 'POST'])
def ai_fertilizer():
    result = None
    if request.method == 'POST':
        soil_type = request.form.get('soil_type', 'Red Loam')
        ph = float(request.form.get('ph', 6.5))
        n = float(request.form.get('nitrogen', 30))
        p = float(request.form.get('phosphorus', 20))
        k = float(request.form.get('potassium', 20))
        target_crop = request.form.get('target_crop', 'Tomato')
        
        result = recommend_fertilizer(soil_type, ph, n, p, k, target_crop)
        
    return render_template('ai_fertilizer.html', result=result)

@main_bp.route('/ai/disease-detection', methods=['GET', 'POST'])
def ai_disease():
    """
    AI Plant Disease Diagnostic View Controller
    Assigned Lead: Mahadev Naik (Project Lead; AI/ML & Disease Detection)
    Milestone: AI Disease Detection Backend Integration Planning (18 August 2026)

    Receives crop leaf image uploads and dispatches inputs to the AI inference engine.
    """
    diagnosis = None
    if request.method == 'POST':
        crop_name = request.form.get('crop_name', 'Tomato')
        symptom_input = request.form.get('symptoms', '')
        file = request.files.get('crop_image')
        filename = file.filename if file else 'sample_leaf.jpg'
        
        diagnosis = detect_disease(crop_name, filename, symptom_input)
        
    return render_template('ai_disease.html', diagnosis=diagnosis)

@main_bp.route('/apmc-prices')
def apmc_prices():
    prices = MarketPrice.query.order_by(MarketPrice.date_updated.desc()).all()
    districts = db.session.query(MarketPrice.district).distinct().all()
    districts = [d[0] for d in districts]
    return render_template('apmc_prices.html', prices=prices, districts=districts)

@main_bp.route('/schemes')
def schemes():
    schemes_list = GovtScheme.query.order_by(GovtScheme.date_posted.desc()).all()
    return render_template('schemes.html', schemes=schemes_list)

@main_bp.route('/forum', methods=['GET', 'POST'])
def forum():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            flash('Please login to post a question on the forum.', 'warning')
            return redirect(url_for('auth.login'))
            
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        category = request.form.get('category', 'General')
        
        if title and content:
            post = ForumPost(
                user_id=current_user.id,
                title=title,
                content=content,
                category=category
            )
            db.session.add(post)
            db.session.commit()
            flash('Your question has been published to the community!', 'success')
            return redirect(url_for('main.forum'))
            
    posts = ForumPost.query.order_by(ForumPost.created_at.desc()).all()
    return render_template('forum.html', posts=posts)

@main_bp.route('/forum/post/<int:post_id>', methods=['POST'])
@login_required
def add_forum_comment(post_id):
    comment_text = request.form.get('comment', '').strip()
    if comment_text:
        is_officer = current_user.role == 'officer'
        comment = ForumComment(
            post_id=post_id,
            user_id=current_user.id,
            comment=comment_text,
            is_officer_verified=is_officer
        )
        db.session.add(comment)
        db.session.commit()
        flash('Reply posted successfully.', 'success')
    return redirect(url_for('main.forum'))

@main_bp.route('/weather')
def weather():
    weather_data = [
        {"district": "Mandya", "temp": 28, "condition": "Partly Cloudy", "icon": "fa-cloud-sun", "humidity": 68, "wind": "12 km/h", "rain_prob": "25%", "advisory": "Ideal Kharif Ragi sowing weather. Irrigation recommended for paddy fields."},
        {"district": "Mysuru", "temp": 27, "condition": "Light Showers", "icon": "fa-cloud-sun-rain", "humidity": 74, "wind": "15 km/h", "rain_prob": "60%", "advisory": "Drain excess water from legume fields to prevent root rot."},
        {"district": "Shivamogga", "temp": 25, "condition": "Heavy Rain", "icon": "fa-cloud-showers-heavy", "humidity": 88, "wind": "22 km/h", "rain_prob": "90%", "advisory": "Arecanut plantation fungicide spray recommended post-rain."},
        {"district": "Kolar", "temp": 30, "condition": "Sunny", "icon": "fa-sun", "humidity": 55, "wind": "10 km/h", "rain_prob": "10%", "advisory": "Maintain regular drip irrigation for tomato and vegetable crops."},
        {"district": "Davanagere", "temp": 29, "condition": "Windy & Sunny", "icon": "fa-wind", "humidity": 60, "wind": "18 km/h", "rain_prob": "15%", "advisory": "Monitor maize crops for Fall Armyworm outbreaks due to dry wind."}
    ]
    return render_template('weather.html', weather_data=weather_data)

@main_bp.route('/news')
def news():
    news_items = [
        {
            "id": 1,
            "title": "Karnataka Cabinet Approves ₹10,000/ha Incentive for Millet Growers under Raitha Siri",
            "category": "Govt Policy",
            "date": "2026-08-08",
            "summary": "The Karnataka Agriculture Department has released funding for Ragi, Foxtail, and Bajra farmers across Mandya, Hassan, and Tumakuru districts.",
            "source": "State Agri Bulletin",
            "icon": "fa-seedling"
        },
        {
            "id": 2,
            "title": "Shivamogga & Channagiri APMC Mandis Record +8.5% Surge in Arecanut Prices",
            "category": "Market Trends",
            "date": "2026-08-07",
            "summary": "Highest auction prices recorded at ₹47,500/Quintal due to strong domestic confectionery and commercial demand.",
            "source": "Mandi Wire",
            "icon": "fa-chart-line"
        },
        {
            "id": 3,
            "title": "Bhoomi Online RTC Portal Parihara Compensation Direct Bank Transfer Live",
            "category": "Scheme Alert",
            "date": "2026-08-06",
            "summary": "Farmers can verify survey numbers and receive direct DBT drought Parihara compensation by linking Aadhaar with Pahani records.",
            "source": "Bhoomi News",
            "icon": "fa-building-columns"
        },
        {
            "id": 4,
            "title": "AI Crop & Disease Detection Advisory Issued for Central Karnataka Maize Fields",
            "category": "Agromet Advisory",
            "date": "2026-08-05",
            "summary": "Farmers urged to utilize smartphone camera diagnosis tools to detect early Fall Armyworm symptoms before pest spreading.",
            "source": "UAS Dharwad Research",
            "icon": "fa-camera"
        }
    ]
    return render_template('news.html', news_items=news_items)

@main_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        district = request.form.get('district', '').strip()
        if current_user.is_authenticated and district:
            current_user.district = district
            try:
                db.session.commit()
            except Exception:
                db.session.rollback()
        flash('Application preferences and profile settings saved successfully!', 'success')
        return redirect(url_for('main.settings'))
    return render_template('settings.html')

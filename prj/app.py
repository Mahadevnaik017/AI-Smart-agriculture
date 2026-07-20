# ========================================================================================
# AI-Driven Smart Agriculture & Micro-crop Advisory System (Mojara)
# Module: Application Factory & Core Server Architecture (app.py)
# Assigned Engineer: Kiran Muttappa Andani
# Responsibility: Backend, MySQL Database, Weather API & System Integration
# Milestone: Backend architecture and API integration planning (20 July 2026)
# ========================================================================================
import os
from flask import Flask, render_template, request, session
from flask_login import LoginManager, current_user
from config import Config
from models import db, User, CartItem, Category, AgriQuote

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Initialize extensions
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'warning'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
    # Context Processors for Templates
    @app.context_processor
    def inject_global_data():
        cart_count = 0
        if current_user.is_authenticated:
            cart_count = CartItem.query.filter_by(buyer_id=current_user.id).count()
        all_categories = Category.query.all()
        current_lang = session.get('lang', 'en')
        try:
            agri_quotes = AgriQuote.query.filter_by(is_active=True).order_by(AgriQuote.id.desc()).all()
        except Exception:
            agri_quotes = []
        return {
            'cart_count': cart_count,
            'all_categories': all_categories,
            'current_lang': current_lang,
            'agri_quotes': agri_quotes,
            'current_year': 2026
        }
        
    # Language Toggle Route
    @app.route('/set-language/<lang>')
    def set_language(lang):
        if lang in ['en', 'kn']:
            session['lang'] = lang
        referrer = request.referrer or '/'
        return render_template('base.html') if False else app.redirect(referrer)
        
    # Register Blueprints
    from routes.auth import auth_bp
    from routes.main import main_bp
    from routes.dashboard import dashboard_bp
    from routes.api import api_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)
    
    # Error Handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404
        
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500
        
    return app

if __name__ == '__main__':
    app = create_app()
    print("[+] Starting Mojara Agriculture Platform on http://127.0.0.1:5000 ...")
    app.run(debug=True, port=5000)

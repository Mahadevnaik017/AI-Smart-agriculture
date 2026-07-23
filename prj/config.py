# ========================================================================================
# AI-Driven Smart Agriculture & Micro-crop Advisory System (Mojara)
# Module: System Environment & Database Configuration (config.py)
# Assigned Engineer: Kiran Muttappa Andani
# Milestone: Environment configuration and database connector planning (23 July 2026)
# ========================================================================================
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mojara-secret-key-agriculture-2026-secure'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///mojara.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload

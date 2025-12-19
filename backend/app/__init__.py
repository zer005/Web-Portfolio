from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    jwt.init_app(app)

    # Register blueprints
    from app.routes import auth, profile, projects, skills, experience, contact

    app.register_blueprint(auth.bp, url_prefix="/api/auth")
    app.register_blueprint(profile.bp, url_prefix="/api/profile")
    app.register_blueprint(projects.bp, url_prefix="/api/projects")
    app.register_blueprint(skills.bp, url_prefix="/api/skills")
    app.register_blueprint(experience.bp, url_prefix="/api/experience")
    app.register_blueprint(contact.bp, url_prefix="/api/contact")

    return app

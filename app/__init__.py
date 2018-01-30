#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-21,21:38"
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_mail import Mail
from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'auth.auth'

def create_app():
    app = Flask(__name__)
    app.config.from_object (Config)
    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    Config.init_app(app)
    login_manager.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix="/auth")


    return app




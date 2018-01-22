#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-21,21:38"
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_moment import Moment
from flask_mail import Mail


bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object (Config)
    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    Config.init_app(app)
    from .main import main
    app.register_blueprint(main)


    return app




#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-21,21:31"
from flask import render_template
from flask_script import Manager
from app import create_app,db
from flask_migrate import MigrateCommand,Migrate
from app.models import User,Role
app = create_app()
manage = Manager(app)
migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)
@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Role = Role)

if __name__ == '__main__':
    manage.run()

#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-21,21:38"
from flask import session,redirect,url_for,render_template
from . import main
from .forms import NameForm
from ..models import User
from .. import db

@main.route("/",methods = ["GET","POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.name.data).first()
        if not user:
            user = User(username = form.name.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
        else:
            session["known"] = True
        session["name"] = form.name.data
        return redirect(url_for('main.index'))
    return render_template('index.html',form = form,name = session.get("name"),known = session.get("known",False))


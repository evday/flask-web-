#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-29,7:42"

from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,logout_user,login_required
from . import auth
from.forms import LoginForm
from ..models import User

@auth.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.data.get("email")).first()
        if user and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            next = request.args.get("next")
            if not next or not next.startswith("/"):
                next = url_for("main.index")
            return redirect(next)
        flash("用户名或密码错误!")
    return render_template("auth/login.html",form = form)

@auth.route("/logout")
def logout():
    logout_user()
    flash("您已经退出登录!")
    return redirect(url_for("main.index"))
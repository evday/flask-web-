#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-29,7:42"

from flask import render_template
from . import auth

@auth.route("/login")
def login():
    return render_template("auth/login.html")
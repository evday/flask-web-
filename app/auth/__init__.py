#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-29,7:41"
from flask import Blueprint

auth = Blueprint("auth",__name__)

from . import views
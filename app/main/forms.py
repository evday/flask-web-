#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-21,21:38"
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField(
        label = "姓名",validators = [DataRequired("姓名不能为空!")]
    )
    submit = SubmitField("提交")
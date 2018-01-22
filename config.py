#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-21,21:31"
import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = os.urandom (24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = True


    @staticmethod
    def init_app(app):
        pass

# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import os
import uuid

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """

    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def upload_data():
    print db.tables
    form = SQLFORM(db.master_table, fields=['table_name','upload_data'])
    if form.process().accepted:
        #filter_table(form)
        response.flash = 'Form Accepted'
        #display_table()
        """session.upload_data = form.vars.upload_data"""
    elif form.errors:
        response.flash = 'Upload Form Error'
    return dict(form = form)

def filter_table(form):
    if form.vars.upload_data is not None:
        f = open("applications/Visualizr/static/" + form.vars.upload_data)
    rows = f.readlines()
    line = rows[0].strip()
    columns = line.split(',')
    tablename = form.vars.table_name
    #tablename = 'standss'
    db.define_table(tablename, *[Field(c) for c in columns])
    for r in range(1,len(rows)):
        row = rows[r].strip()
        entries = row.split(',')
        for index in range(0,len(entries)):
            db[tablename][columns[index]] = entries[index]
    #master_entry = db(db.master_table.upload_data == form.vars.upload_data).update(table_id = tablename)

def display_table():
    print db.tables
    print db['standss']['stand']

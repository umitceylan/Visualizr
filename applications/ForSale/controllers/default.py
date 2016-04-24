#########################################################################
# Umit Ceylan
# UCSC ID #1437198
# umceylan
# 2/3/2016
#########################################################################


def index():
    list = db().select(db.image.ALL, orderby = db.image.title)
    return dict(list = list)

def show():
    image = db.image(request.args(0, cast = int)) or redirect(URL('index'))
    return dict(image = image)

#@auth.requires_login()
def post_new_ad():
    form = SQLFORM(db.image)
    if form.process().accepted:
        response.flash = "Contratulations!"
        response.flash = "You have successfuly posted your ad!"

    return dict(form =form)

def create_table(form):
    print form.vars.file.file.readline()
    print form.vars.id
    # actually, have to do the form creation manually, can't put directly into table.  bbs

def test():
    form=SQLFORM(db.test,fields=['file'])
    # if request.vars.file!=None:
    #     form.vars.filename=strip_path_and_sanitize(request.vars.file.filename)
    if form.process(onvalidation=create_table).accepted:
        response.flash='success!'
    return dict(form=form)


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

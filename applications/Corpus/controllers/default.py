# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    form = FORM(INPUT(_type="submit",_value='asd'),
               )

    '''
    form = SQLFORM.factory(Field('Query1',requires=IS_NOT_EMPTY()),
                           Field('Query2','date',requires=IS_NOT_EMPTY())).process()
    if form.accepted:
        #session.flash = 'Form accepted'
        redirect(URL('other',vars={'Query1':form.vars.Query1,
                                   'Query2':form.vars.Query2}))
    elif form.errors:
        #response.flash = 'Form containt errors'
        pass
    else:
        #response.flash = 'Form displayed for the first time'
        pass
    '''
    return locals()
    #redirect(URL('other',args=['hello',':v'],vars={'a':'test','b':123}))
    #return "AOOAOAOAOAOAO"

def other():
    '''
    esto iría en index
    <form action="{{=URL('other')}}">
    Your  name?
    <input name="y_name"/>
    <br>
    <input type="submit"/>
</form>
    x = request.args
    y = request.vars
    return "totototoo r=%s %s" % (x,SPAN(y))
    '''
    message = 'Welcome, %s! B=%s' % (request.vars.Query1,request.vars.Query2)
    return locals()

def btn1():
    
    
    return locals()

def btn2():
    return locals()


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

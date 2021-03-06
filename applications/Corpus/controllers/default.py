# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import os,sys


def index():
    #response.flash = os.getcwd()
    return locals()

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
    path = os.getcwd()
    response.flash = path
    model_tf = tfIdf()
    l = model_tf.search(request.vars.word)
    probs={}
    for i,j in l:
        probs[i]=j
    #ver como recibir argumentos
    response.flash = 'Frase: '+request.vars.word
    
    
    message = 'WORD %s!' % (request.vars.word)
    return dict(form=sorted(probs.items(),reverse=True))
    '''
    
    response.flash = os.getcwd()+'/applications/Corpus'
    path=os.getcwd()
    sys.path.append(os.getcwd()+'/applications/Corpus/controllers')
    sys.path.append(os.getcwd()+'/applications/Corpus/controllers/')
    os.chdir(os.getcwd()+'/applications/Corpus/controllers/')
    from tfIdf import tfIdf
    model = tfIdf()
    os.chdir(path)
    l = model.search(request.vars.Palabra)
    probs={}
    for i,j in l:
        if i != 0:
            probs[i]=j
    os.chdir(path)#
    message = 'WORD %s!' % (request.vars.Palabra)
    return dict(form=sorted(probs.items(),reverse=True))

def infmutua():
    response.flash = os.getcwd()
    path=os.getcwd()
    sys.path.append(os.getcwd()+'/applications/Corpus/controllers')
    os.chdir(os.getcwd()+'/applications/Corpus/controllers')
    from MI import MI
    model = MI()
    mi = model.eval(request.vars.Palabra1,request.vars.Palabra2)
    message = 'WORD %s %s' % (request.vars.Palabra1,request.vars.Palabra2)
    os.chdir(path)
    return dict(mi=mi)

def colocaciones():#concordancias
    response.flash = os.getcwd()
    message=request.vars.Query
    path=os.getcwd()
    sys.path.append(os.getcwd()+'/applications/Corpus/controllers')
    sys.path.append(os.getcwd()+'/applications/Corpus/controllers/')
    os.chdir(os.getcwd()+'/applications/Corpus/controllers')
    from concordance import get
    res = get(request.vars.Query).split('\n')
    os.chdir(path)
    return dict(res=res)

def feelings():
    response.flash = os.getcwd()
    message=request.vars.Palabra
    path=os.getcwd()
    sys.path.append(os.getcwd()+'/applications/Corpus/controllers')
    sys.path.append(os.getcwd()+'/applications/Corpus/controllers/')
    os.chdir(os.getcwd()+'/applications/Corpus/controllers')
    from Bayes import Bayes
    model = Bayes()
    tmp = model.evalStr(request.vars.Palabra)
    os.chdir(path)
    return dict(tmp=tmp)

def btn1():
    #response.flash= os.getcwd()+'/Backend'
    form = SQLFORM.factory(Field('Palabra',requires=IS_NOT_EMPTY())).process()
    if form.accepted:
        redirect(URL('other',vars={'Palabra':form.vars.Palabra}))
    return locals()

def btn2():
    form = SQLFORM.factory(Field('Palabra1',requires=IS_NOT_EMPTY()),
                           Field('Palabra2',requires=IS_NOT_EMPTY())).process()
    if form.accepted:
        redirect(URL('infmutua',vars={'Palabra1':form.vars.Palabra1,'Palabra2':form.vars.Palabra2}))
    return dict(form=form)

def btn3():
    form = SQLFORM.factory(Field('Query',requires=IS_NOT_EMPTY())).process()
    if form.accepted:
        redirect(URL('colocaciones',vars={'Query':form.vars.Query}))
    return dict(form=form)

def btn4():
    response.flash= os.getcwd()+'/Backend'
    form = SQLFORM.factory(Field('Palabra',requires=IS_NOT_EMPTY())).process()
    if form.accepted:
        redirect(URL('feelings',vars={'Palabra':form.vars.Palabra}))
    return locals()

def btn5():
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

# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def erreur():
    return "page erreur"


def get_categorie():
    nom_categorie = request.args(0)
    categorie = db.produit(url=nom_categorie)
    if not categorie:
        redirect(URL('erreur'))
    return categorie



def bienvenue():
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom,limitby=(0, 5) )
    response.title= "Votre caftan pas chère"
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = "invalid email!"
    return dict(title=response.title,
                caftans=caftans,
                form3=form3)

def acceuil():
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom,limitby=(0, 5) )
    response.title= "Votre caftan pas chère"
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return dict(title=response.title,
                caftans=caftans,
                form3=form3)


def caftan_en_location():
    import textwrap
    locat = T("Caftan en location")
    caftans = db(db.produit.types == locat).select(orderby=~db.produit.nom)
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return dict(caftans=caftans,
                textwrap=textwrap,
                locat=locat,
                form3=form3)


def caftan_en_vente():
    import textwrap
    locat = T("Caftan en vente")
    caftans = db(db.produit.types == locat).select(orderby=~db.produit.nom)
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return dict(caftans=caftans,
                textwrap=textwrap,
                locat=locat,
                form3=form3)



def robe_de_soiree_en_location():
    import textwrap
    locat = "Robe de soirée en location"
    caftans = db(db.produit.types == locat).select(orderby=~db.produit.nom)
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return dict(caftans=caftans,
                textwrap=textwrap,
                locat=locat,
                form3=form3)


def robe_de_soiree_en_vente():
    import textwrap
    locat = "Robe de soirée en vente"
    caftans = db(db.produit.types == locat).select(orderby=~db.produit.nom)
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return dict(caftans=caftans,
                textwrap=textwrap,
                locat=locat,
                form3=form3)



def caftan_en_location_grande_taille():
    import textwrap
    locat = "Djellaba"
    caftans = db(db.produit.types == locat).select(orderby=~db.produit.nom)
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return dict(caftans=caftans,
                textwrap=textwrap,
                locat=locat,
                form3=form3)


def caftan_en_vente_grande_taille():
    import textwrap
    locat = "Guandoura"
    caftans = db(db.produit.types == locat).select(orderby=~db.produit.nom)
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return dict(caftans=caftans,
                textwrap=textwrap,
                locat=locat,
                form3=form3)


def contact():
    form = SQLFORM(db.contact)
    if form.process().accepted:
        response.flash = "Demande prise en compte"
    elif form.errors:
        response.flash = ""
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = "invalid email!"
    return dict(form=form, 
                form3=form3)

def vue():
    id = request.args(0)
    caftans = db(db.produit.url == id).select()
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return dict(caftans=caftans, 
                form3=form3)

def blog():
    blogs =  db().select(db.blog.ALL)
    return dict(blogs=blogs)


def vue_blog():
    id = request.args(0)
    caftans = db(db.blog.url_titre == id).select()
    return dict(caftans=caftans)


def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki()

# ---- Action for login/register/etc (required for auth) -----
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

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

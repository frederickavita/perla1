# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)


def widget(**kwargs):
    return lambda field, value, kwargs=kwargs: SQLFORM.widgets[field.type].widget(field, value, **kwargs)




db.define_table('contact',
Field('nom', 'string'),
Field('email'),
Field('sujet', 'string'),
Field('messages', 'text'))


db.contact.nom.requires = IS_NOT_EMPTY(error_message=T('Ne peut être vide'))
db.contact.email.requires  = IS_EMAIL(error_message=T('Votre email est invalide'))
db.contact.sujet.requires = IS_NOT_EMPTY(error_message=T('Ne peut être vide'))
db.contact.messages.requires = IS_NOT_EMPTY(error_message=T('Ne peut être vide'))




db.define_table('newsletter',
    Field('email',requires=IS_NOT_IN_DB(db, 'newsletter.email')))








produites = ["Bijoux", 'Djellaba', "accessoires", "Caftan en location", "Caftan en vente",
           "Robe de soirée en location", "Robe de soirée en vente", "Caftan blanche","Guandoura" ]


db.define_table('produit',
Field('nom', 'string'),
Field('descriptif', 'text'),
Field('prix_hors_taxe', 'double'),
Field('tva', 'double'),
Field('prix_total', 'double'),
Field('taille'),
Field('types'),
Field('locations', 'boolean'),
Field('devise'),
Field('couleur'),
Field('fabrique'),
Field('tag', 'string'),
Field('tag1', 'string') ,
Field('tag2', 'string'),
Field('tag3', 'string'),
Field('photo1', 'upload'),
Field('photo2', 'upload'),
Field('photo3', 'upload'),
Field('stock', 'integer'),
Field('url', 'string'),
auth.signature)



db.define_table('facturation',
Field('users', 'reference auth_user'),
Field('produit', 'reference produit'),
Field('adresse', 'string', widget=widget(_placeholder='One-two word description', _readonly=False)),
Field('code_postal', 'string'),
Field('ville', 'string'),
auth.signature)

db.facturation.users.writable = db.facturation.users.readable = False

db.facturation.produit.writable = db.facturation.produit.readable = False


db.facturation.adresse.requires = IS_NOT_EMPTY()
db.facturation.code_postal.requires = IS_NOT_EMPTY()
db.facturation.ville.requires = IS_NOT_EMPTY()



db.define_table('livraison',
Field('users', 'reference auth_user'),
Field('produit', 'reference produit'),
Field('adresse', 'string',widget=widget(_placeholder='8 rue du marche', _readonly=False)),
Field('code_postal', 'string',widget=widget(_placeholder='7700', _readonly=False)),
Field('ville', 'string',widget=widget(_placeholder='Melun', _readonly=False)),
auth.signature)


db.livraison.users.writable = db.livraison.users.readable = False

db.livraison.produit.writable = db.livraison.produit.readable = False



db.livraison.adresse.requires = IS_NOT_EMPTY()
db.livraison.code_postal.requires = IS_NOT_EMPTY()
db.livraison.ville.requires = IS_NOT_EMPTY()


taille = ['M', 'L', 'XL', 'FS', 'S']
db.produit.taille.requires = IS_IN_SET(taille,zero=T('Faite un choix'),
         error_message='must be a or b or c')


db.produit.types.requires = IS_IN_SET(produites,zero=T('Faite un choix'),
         error_message='must be a or b or c')

db.produit.types.default = produites[0]
db.produit.taille.default = taille[0]

session.cart = session.cart or {}



db.define_table('achat',
    Field('acheteur', 'reference auth_user'),
    Field('address'),
    Field('ville'),
    Field('code_postal'),
    Field('produit', 'list:string'),
    Field('pays', 'string', default="france"),
    Field('prix_livraison','decimal(10,2)',readable=False,writable=False),
    Field('quantite','decimal(10,2)',readable=False,writable=False),
    Field('total_prix','decimal(10,2)',readable=False,writable=False),
    Field('total_tva','decimal(10,2)',readable=False,writable=False),
    Field('total_balance','decimal(10,2)',readable=False,writable=False),
    Field('montant_paye','decimal(10,2)',readable=False,writable=False),
    Field('payment_id',readable=False,writable=False),
    Field('paid_le','datetime',readable=False,writable=False),
    Field('status',requires=IS_IN_SET(('submitted','shipped','received','returned')),
          default='submitted',readable=False,writable=False),
    Field('notes','text'),
    auth.signature)




db.define_table("blog",
Field("titre", "string"),
Field("url_titre", "string"),
Field("titre_description", 'string'),
Field("dating", "string"),
Field("img", "upload"),
Field("img_name", "string"),
Field("post", "text"))




User  = db.auth_user
me, a0, a1 = auth.user_id, request.args(0), request.args(1)
def name_of(user): return '%(first_name)s' % user



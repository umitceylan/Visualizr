#########################################################################
# Umit Ceylan
# UCSC ID #1437198
# umceylan
# 2/3/2016
#########################################################################


db = DAL("sqlite://storage.sqlite")

db.define_table("image",
   Field("name"),
   Field("phone_number"),
   Field("email"),
   Field("date"),             
   Field("title", unique=True),
   Field("description", "text"),
   Field("file", "upload"),
   Field("category"), 
   Field("price", "double"),
   Field("status", default = False), 
   format = '%(title)s')

db.define_table('post',
   Field('image_id', 'reference image'))
   
db.post.image_id.requires = IS_IN_DB(db, db.image.id, '%(title)s')

db.image.email.requires = IS_EMAIL()
db.image.phone_number.requires = IS_MATCH('^1+-\d{3}\-?\d{3}\-?\d{4}$', error_message='Please enter X-XXX-XXX-XXXX format')


db.image.title.requires = IS_NOT_IN_DB(db, db.image.title)
db.image.category.requires = IS_IN_SET(["Car", "Bike" , "Book" , "Music" , "Outdoors", "Household", "Misc."])
db.image.price.requires = IS_FLOAT_IN_RANGE(0, 100000.0 , error_message='The price should be in the range 0..100000')
db.image.status.requires = IS_IN_SET(["Sold", "Still Available"])



db.post.image_id.writable = db.post.image_id.readable = False


from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username = False, signature = False)

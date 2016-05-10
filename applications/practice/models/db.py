db = DAL("sqlite://storage.sqlite")

db.define_table("friends",
   Field("name"),
   Field("last_name"))

db.friends.name.writable = False
db.friends.last_name.writable = False

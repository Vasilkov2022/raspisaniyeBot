from tinydb import TinyDB, Query\

db = TinyDB('db.json')
# table = db.table('User')

print(db.all())

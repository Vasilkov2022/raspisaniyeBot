from tinydb import TinyDB, Query
db = TinyDB('db.json')
schedule = Query()
print(db.search(schedule.dayOfWeekString == 'Mon'))
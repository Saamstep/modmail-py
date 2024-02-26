from tinydb import TinyDB, Query

# ************************************************************** #
#                            USER DATA
# * id | status | lastReply | assigned_to | channel_id | hud_id
# ************************************************************** #

db = TinyDB('./tickets.json')
db.table("tickets")

def new_ticket(uid, channel_id) -> int:
  entry = db.insert({'id': uid, 'status': "NEW", 'lastReply': 'USER', 'assigned_to': None, 'channel_id': channel_id, 'hud_id': None})
  return entry

def find_user(uid):
  User = Query()
  return db.search(User.id == uid)


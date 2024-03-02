from peewee import *

# ************************************************************** #
#                            USER DATA
# * id | status | lastReply | assigned_to | channel_id | hud_id
# ************************************************************** #

db = SqliteDatabase("tickets.db")

class BaseModel(Model):
  class Meta:
    database = db

class Ticket(BaseModel):
  id = IntegerField()
  status = TextField()
  lastReply = TextField()
  assigned_to = IntegerField()
  channel_id = IntegerField()
  hud_id = IntegerField()

db.connect()
db.create_tables([Ticket])

def new_ticket(u, channel) -> int:
  entry = Ticket.create(id=u.id, status="NEW", lastReply="p", assigned_to=0, channel_id=channel.id, hud_id=0)
  return entry

def find_user(u):
  query = db.search(where('id') == u.id)
  return query

def delete_ticket(channel_id) -> None:
  db.remove(where('channel_id' == channel_id))
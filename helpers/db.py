import sqlite3

# ************************************************************** #
#                            USER DATA
# * id | status | lastReply | assigned_to | channel_id | hud_id
# ************************************************************** #

db = sqlite3.connect("bot.db")

cursor = db.cursor()

tableCheck = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tickets'").fetchall()

if len(tableCheck) == 0:
  cursor.execute("CREATE TABLE tickets (id TEXT, status TEXT, lastReply INTEGER, assigned_to TEXT, channel_id TEXT, hud_id TEXT)")

cursor.close()

def new_ticket(u, channel) -> int:
  cursor = db.cursor()
  entry = cursor.execute("INSERT INTO tickets VALUES(?,'NEW',0,'NA',?,'NULL')", (u.id, channel.id))
  db.commit()
  cursor.close()
  return entry

def find_user(u) -> bool:
  cursor = db.cursor()
  query = cursor.execute(
    "SELECT * FROM tickets WHERE id = ?",
    (u.id,),
    ).fetchall()
  cursor.close()
  if(len(query) > 0):
    return True
  else:
    return False
  
def getUserId(ch):
  cursor = db.cursor()
  query = cursor.execute(
    "SELECT id FROM tickets WHERE channel_id = ?",
    (ch,),
    ).fetchone()
  cursor.close()
  if(len(query) > 0):
    return str(query[0])
  else:
    return None
  
def getTicketChannel(u):
  cursor = db.cursor()
  query = cursor.execute(
    "SELECT channel_id FROM tickets WHERE id = ?",
    (u.id,),
    ).fetchone()
  cursor.close()
  if(len(query) > 0):
    return str(query[0])
  else:
    return None

def delete_ticket(channel_id) -> None:
  cursor = db.cursor()
  query = cursor.execute(
    "DELETE FROM tickets WHERE channel_id = ?",
    (channel_id,),
    )
  cursor.close()
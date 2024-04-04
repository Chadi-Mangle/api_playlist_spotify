from secrets import playlist_lecrew_id, playlist_jour_id, playlist_nuit_id
from delete import DeleteSongs
from add import AddSongs
from datetime import datetime

print("Le script est en marche...")

while 1:
	if float(datetime.now().strftime('%H.%M%S'))+ 2 == 7: 
		d = DeleteSongs(playlist_lecrew_id)
		a = AddSongs(playlist_jour_id, playlist_lecrew_id)
		d.call_refresh()
		a.call_refresh()
	elif float(datetime.now().strftime('%H.%M%S'))+ 2 == 19:
		d = DeleteSongs(playlist_lecrew_id)
		a = AddSongs(playlist_nuit_id, playlist_lecrew_id)
		d.call_refresh()
		a.call_refresh()
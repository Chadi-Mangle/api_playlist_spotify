import json 
import requests
from secrets import spotify_user_id, playlist_lecrew_id, playlist_jour_id, playlist_nuit_id
from refresh import Refresh

class AddSongs:
	def __init__(self, playlist_id, playlist_id2): 
		self.user_id =spotify_user_id 
		self.token = ""
		self.playlist_id = playlist_id
		self.playlist_id2 = playlist_id2
		self.tracks = ""
		self.new_playlist_id = ""

	def find_songs(self): 
		"""Prend les éléments de la playlist et les ajoutent a une liste"""
		
		query = "https://api.spotify.com/v1/playlists/{}/tracks".format(self.playlist_id)
		response = requests.get(query, 
															headers={"Content-Type": "application/json", 
																			 "Authorization":"Bearer {}".format(self.spotify_token)})

		response_json = response.json()
		#print(json.dumps(response_json, sort_keys=4, indent=0))
		#print(response)

		print("Recherche des sons de la playlist...")
		
		for i in response_json["items"]: 
			print(i['track']['name'] + ' : ' + i['track']['uri'])
			self.tracks += (i['track']['uri'] + ",")
		self.tracks = self.tracks[:-1]
		#print('\n' + self.tracks)
		
		self.add_song()

	
	def add_song(self): 
		"""Ajoute les sons de l'ancienne playlist a la nouvelle"""

		self.new_playlist_id = self.playlist_id2

		query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(self.new_playlist_id, self.tracks)
		#print(query)
		response = requests.post(query, headers={"Content-Type": "application/json", 
																			 				"Authorization":"Bearer {}".format(self.spotify_token)})
		print(response.json)
		print('Ajout des sons a la playlist')
	

	def call_refresh(self): 
		"""Donne un accès a l'API spotify"""

		print("accès a l'api de Spotify en cours...")
		
		refreshCaller = Refresh()
		self.spotify_token = refreshCaller.refresh()

		self.find_songs()
		




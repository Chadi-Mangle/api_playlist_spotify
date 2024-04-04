import json 
import requests
from secrets import spotify_user_id, playlist_lecrew_id, playlist_jour_id, playlist_nuit_id
from refresh import Refresh

class DeleteSongs: 
	def __init__(self, playlist_id): 
		self.user_id = spotify_user_id
		self.playlist_id = playlist_id
		self.tracks = []
		

	def call_refresh(self): 
		"""Donne un accès a l'API spotify"""

		print("Accès a l'api de Spotify en cours...")
		
		refreshCaller = Refresh()
		self.spotify_token = refreshCaller.refresh()
		self.find_songs()

	
	def find_songs(self): 
		"""Prend les morceaux d'une playlist et les ajoutent a une liste de dictionnaire"""
		
		query = "https://api.spotify.com/v1/playlists/{}/tracks".format(self.playlist_id)
		response = requests.get(query, 
															headers={"Content-Type": "application/json", 
															"Authorization":"Bearer {}".format(self.spotify_token)})

		response_json = response.json()
		#print(json.dumps(response_json, sort_keys=4, indent=0))
		#print(response)
		print("Recherche des sons de la playlist...")

		print("\nMorceaux de la playlist:")
		for i in response_json["items"]: 
			print(i['track']['name'] + ' : ' + i['track']['uri'])
			self.tracks.append({'uri': str(i['track']['uri'])})
		print("")
		#print('\n', self.tracks)
		self.del_song()

	
	def del_song(self): 
		"""Supprime les morceaux d'une playlist"""
		json_data = {
				'tracks': self.tracks,
		}
		print("Suppression des morceaux...")
		query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(self.playlist_id)
		response = requests.delete(query, headers = {'Accept': 'application/json',
															'Authorization': 'Bearer {}'.format(self.spotify_token),},
															json=json_data)
		print("Les morceaux ont bien été supprimé.")
		response_json = response.json 
		#print(response_json)

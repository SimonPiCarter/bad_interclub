
import json

from bo.player import Player

def readPlayerJson(file):
	players = []

	with open(file) as f:
		data = json.load(f)
		for elt in data:
			players.append(Player(elt["name"]))

	return players


import json

from bo.player import Player

def readPlayerJson(file):
	players = []

	with open(file) as f:
		data = json.load(f)
		players = readPlayerData(data)

	return players

def readPlayerData(data):
	players = []

	for elt in data:
		players.append(Player(elt["name"]))

	return players


import json

from bo.match import Match

def readMatchJson(file, vectPlayers):
	matches = []

	with open(file) as f:
		data = json.load(f)
		matches = readMatchData(data, vectPlayers)

	return matches

def readMatchData(data, vectPlayers):
	matches = []

	for elt in data:
		playerInMatch = []
		for player in elt["players"]:
			for candidate in vectPlayers:
				if candidate.name == player:
					playerInMatch.append(candidate)
		matches.append(Match(elt["name"], playerInMatch))

	return matches

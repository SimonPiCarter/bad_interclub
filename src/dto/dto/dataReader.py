
import json

from dto.matchReader import readMatchData
from dto.playerReader import readPlayerData

def readDataJson(file):
	players = []
	matches = []

	with open(file) as f:
		data = json.load(f)
		players = readPlayerData(data["players"])
		matches = readMatchData(data["matches"], players)

	return (players, matches)


import json

from dto.matchReader import readMatchData
from dto.playerReader import readPlayerData

from bo.constraint import OrderConstraint
from bo.constraint import RankConstraint

def readRankConstraintData(data):
	rankConstraints = []

	for elt in data:
		rankConstraints.append(RankConstraint(elt["name"], elt["matchName"], int(elt["matchRank"])))

	return rankConstraints

def readOrderConstraintData(data):
	orderConstraints = []

	for elt in data:
		orderConstraints.append(OrderConstraint(elt["name"], elt["firstMatch"], elt["secondMatch"]))

	return orderConstraints

def readDataJson(file):
	players = []
	matches = []
	rankConstraints = []
	orderConstraints = []

	with open(file) as f:
		data = json.load(f)
		players = readPlayerData(data["players"])
		matches = readMatchData(data["matches"], players)
		rankConstraints = readRankConstraintData(data["rankConstraints"])
		orderConstraints = readOrderConstraintData(data["orderConstraints"])

	return (players, matches, rankConstraints, orderConstraints)


import json

from dto.matchReader import readMatchData
from dto.playerReader import readPlayerData

from bo.constraint import OrderConstraint
from bo.constraint import RankConstraint

def writeSolution(file, solver, matchVars, goalRankVars, goalOrderVars):
	data = {}
	data["matches"] = []
	data["rankConstraints"] = []
	data["orderConstraints"] = []

	for match in matchVars:
		data["matches"].append({
			"name" : match.match.name,
			"rank" : solver.Value(match.var)
		})
	for var in goalRankVars:
		violated = solver.Value(var) == 0
		data["rankConstraints"].append({
			"name" : var.Name(),
			"violated" : violated
		})
	for var in goalOrderVars:
		violated = solver.Value(var) == 0
		data["orderConstraints"].append({
			"name" : var.Name(),
			"violated" : violated
		})

	with open(file, 'w') as outfile:
		json.dump(data, outfile)

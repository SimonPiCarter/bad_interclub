
from ortools.sat.python import cp_model

from opt.matchVar import MatchVar

def buildObjective(model, matchVars, penVars, matchTime, penTime):
	"""Méthode qui construit la contrainte de nombre de match
		en simultané maximum"""

	maxRank = model.NewIntVar(0, 9999, "maxMatchRank")
	model.AddMaxEquality(maxRank, [matchVar.var for matchVar in matchVars])

	sumPen = sum(penVars)

	model.Minimize(maxRank * matchTime + sumPen * penTime)

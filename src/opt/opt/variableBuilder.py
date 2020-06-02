
from ortools.sat.python import cp_model

from opt.matchVar import MatchVar

def buildMatchVar(model, matchs, nbMatchMax):
	"""Méthode qui construit la contrainte de nombre de match
		en simultané maximum"""
	matchVars = []
	for match in matchs:
		matchVars.append(MatchVar(match, model.NewIntVar(0, nbMatchMax, match.name)))

	return matchVars

def buildPenalisationVar(model, maxRank):
	penVars = []
	for n in range(0,maxRank):
		penVars.append(model.NewIntVar(0, maxRank, "pen_"+str(n)))
	return penVars

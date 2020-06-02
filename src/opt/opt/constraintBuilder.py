
from ortools.sat.python import cp_model

def buildNonConcurrentMatchWithSamePlayerConstraint(model, matchVars):
	"""Méthode qui construit la contrainte interdisant plusieurs matchs en
	même temps pour un joueur"""
	for matchVar1 in matchVars:
		for matchVar2 in matchVars:
			if matchVar1 == matchVar2:
				break
			intersectionPlayer = [value for value in matchVar1.match.players if value in matchVar2.match.players]
			if len(intersectionPlayer) > 0:
				model.Add(matchVar1.var != matchVar2.var)


def buildNbCourtConstraint(model, matchVars, nbCourt, nbMatchMax):
	"""Méthode qui construit la contrainte de nombre de matchs
		en simultanés maximum"""
	for n in range(0,nbMatchMax):
		cardVar = []
		for matchVar in matchVars:
			var = model.NewBoolVar("isMatchRank_" + str(n) + "_" +matchVar.match.name)
			model.Add(matchVar.var == n).OnlyEnforceIf(var)
			model.Add(matchVar.var != n).OnlyEnforceIf(var.Not())
			cardVar.append(var)

		expr = sum([cardVar[i] for i in range(len(cardVar))])
		model.Add(expr <= nbCourt)

def buildPenalisationConstraint(model, matchVars, penVars, maxRank):
	"""Méthode qui construit la contrainte pénalisant plusieurs matchs qui s'enchainent
	 pour un joueur"""
	for matchVar1 in matchVars:
		for matchVar2 in matchVars:
			if matchVar1 == matchVar2:
				continue
			intersectionPlayer = [value for value in matchVar1.match.players if value in matchVar2.match.players]
			if len(intersectionPlayer) > 0:
				matchSuccessive = model.NewBoolVar("isMatchSuccessive_" + matchVar1.match.name + "_" +matchVar2.match.name)
				diff = matchVar1.var - matchVar2.var
				model.Add(diff == 1).OnlyEnforceIf(matchSuccessive)
				model.Add(diff != 1).OnlyEnforceIf(matchSuccessive.Not())

				minRank = model.NewIntVar(0, maxRank, "minVar_"+matchVar1.match.name + "_" +matchVar2.match.name)
				model.AddMinEquality(minRank, (matchVar1.var, matchVar2.var))

				penalisationValue = model.NewIntVar(0, 1, "penalisationSuccessive_"+matchVar1.match.name + "_" +matchVar2.match.name)

				model.AddElement(minRank, penVars, penalisationValue)

				model.Add(penalisationValue == 1).OnlyEnforceIf(matchSuccessive)

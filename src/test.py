from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model

from bo.player import Player
from bo.match import Match
from opt.constraintBuilder import *
from opt.objectiveBuilder import *
from opt.variableBuilder import *

from dto.dataReader import *
from dto.matchReader import *
from dto.playerReader import *

def SimpleMatchProgram():
    """Minimal CP-SAT match."""
    # Creates the model.
    model = cp_model.CpModel()


    (players, matches, rankConstraints, orderConstraints) = readDataJson("../data/data.json")

    maxRank = len(matches)
    nbcourt = 2
    matchTime = 32
    penTime = 15
    goalCost = 10000

    matchVars = buildMatchVar(model, matches, maxRank)
    penVars = buildPenalisationVar(model, maxRank)

    buildNbCourtConstraint(model, matchVars, nbcourt, maxRank)
    buildNonConcurrentMatchWithSamePlayerConstraint(model, matchVars)
    buildPenalisationConstraint(model, matchVars, penVars, maxRank)
    goalRankVars = buildRankConstraint(model, matchVars, rankConstraints)
    goalOrderVars = buildOrderConstraint(model, matchVars, orderConstraints)

    buildObjective(model, matchVars, penVars, matchTime, penTime, goalRankVars, goalOrderVars, goalCost)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        for match in matchVars:
            print(match.match.name+' : %i' % solver.Value(match.var) )
        for var in goalRankVars:
            print(var.Name()+' : %i' % solver.Value(var) )
        for var in goalOrderVars:
            print(var.Name()+' : %i' % solver.Value(var) )



SimpleMatchProgram()

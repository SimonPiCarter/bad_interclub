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


    (players, matches) = readDataJson("../data/data.json")

    maxRank = len(matches)
    nbcourt = 2
    matchTime = 32
    penTime = 15

    matchVars = buildMatchVar(model, matches, maxRank)
    penVars = buildPenalisationVar(model, maxRank)

    buildNbCourtConstraint(model, matchVars, nbcourt, maxRank)
    buildNonConcurrentMatchWithSamePlayerConstraint(model, matchVars)
    buildPenalisationConstraint(model, matchVars, penVars, maxRank)

    buildObjective(model, matchVars, penVars, matchTime, penTime)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        for match in matchVars:
            print(match.match.name+' : %i' % solver.Value(match.var) )



SimpleMatchProgram()

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model

from bo.player import Player
from bo.match import Match
from opt.constraintBuilder import *
from opt.objectiveBuilder import *
from opt.variableBuilder import *

def SimpleSatProgram():
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 3
    x = model.NewIntVar(0, num_vals - 1, 'x')
    y = model.NewIntVar(0, num_vals - 1, 'y')
    z = model.NewIntVar(0, num_vals - 1, 'z')

    # Creates the constraints.
    model.Add(x != y)

    # Creates the objective.
    model.Minimize(x+2*y)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        print('x = %i' % solver.Value(x))
        print('y = %i' % solver.Value(y))
        print('z = %i' % solver.Value(z))

def SimpleMatchProgram():
    """Minimal CP-SAT match."""
    # Creates the model.
    model = cp_model.CpModel()


    player1 = Player("p1")
    player2 = Player("p2")
    print(player1.name)
    print(player2.name)

    match1 = Match("SH1", (player1, player2))
    match2 = Match("SH2", (player1, player2))

    maxRank = 3
    nbcourt = 2
    matchTime = 32
    penTime = 15

    matchVars = buildMatchVar(model, (match1, match2), maxRank)
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

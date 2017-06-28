import protodicho
import tools
import pickle
import sys
import numpy as np

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 
NB_GENER = 10
X = GAME_HEIGHT/2
Y = 130

strat1 = tools.PasseLearningStrat()

expe = protodicho.Experience( Y, X, [ strat1 ] )

expe.start( True )



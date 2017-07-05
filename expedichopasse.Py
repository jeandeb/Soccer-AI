import dichopasse
import tools
import pickle
import sys
import numpy as np

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 
NB_GENER = 10
X = 50
Y = 110
X2 = 90
Y2 = 80

strat1 = tools.PasseLearningStrat()
strat2 = tools.StaticStrategy()

expe = dichopasse.Experience( Y, X, X2, Y2, [ strat1, strat2 ] )

expe.start( True )

print expe.data.state

if( (len(sys.argv) > 1) and (sys.argv[1] == "yes") ) :
	pickle.dump( expe.data.state, open( "expedichopasse.p", "wb" ) )



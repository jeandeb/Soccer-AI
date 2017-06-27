import prototype
import tools
import pickle
import sys
import numpy as np
NB_GENER = 10

strat2 = tools.StaticStrategy()
strat1 = tools.PasseLearningStrat()

expe = prototype.Experience( NB_GENER, [ strat1, strat2 ] )

expe.start( True )

if( (len(sys.argv) > 1) and (sys.argv[1] == "yes") ) :
	pickle.dump( expe, open( "expepasse.p", "wb" ) )
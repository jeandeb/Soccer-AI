import prototype
import tools
import pickle
import sys
import numpy as np
NB_GENER = 20

strat1 = tools.PasseLearningStrat()

expe = prototype.Experience( NB_GENER, [ strat1 ] )

expe.start( False )

print expe.data.state
if( (len(sys.argv) > 1) and (sys.argv[1] == "yes") ) :
	pickle.dump( expe, open( "expetir.p", "wb" ) )
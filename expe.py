import prototype
#from Projet_2I013 import strategy
import tools
import pickle
import numpy as np
NB_GENER = 10

strat1 = tools.StaticStrategy()

expe = prototype.Experience( NB_GENER, [ strat1, strat1 ] )

expe.start( True )
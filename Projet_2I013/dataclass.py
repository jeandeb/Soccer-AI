import numpy as np
from soccersimulator import settings
MAX_X = settings.GAME_WIDTH/2
MAX_Y = settings.GAME_HEIGHT

class discretedata( object ) : 
	

	def __init__( self ) :
		#stex, stepy, stepnorm"
		self.step_x = 3
		self.step_y = 3
		self.nb_x =25
		self.nb_y = 30
		self.tab_proba = np.zeros(( self.nb_x, self.nb_y ))
		self.tab_norm = np.zeros(( self.nb_x, self.nb_y ))

	def nb_x( self ) :
		return self.nb_x

	def nb_y( self ) :
		return self.nb_y

	def get_norm( self, x, y) :

		case_x = ( x - MAX_X)  / self.step_x
		case_y = y/self.step_y 

		return self.tab_norm[ case_x-1 , case_y-1 ]

	def set_norm( self, norm, x, y ) :

		case_x =( x - MAX_X) / self.step_x
		case_y = y/self.step_y 

		self.tab_norm[ case_x-1 , case_y -1] = norm
		

	def get_proba( self, x, y) :

		case_x = ( x - MAX_X)  / self.step_x
		case_y = y/self.step_y 
		tmp = self.tab_proba[ case_x -1, case_y-1 ]
		return tmp

	def set_proba( self, proba, x, y ) :
		case_x = ( x - MAX_X)  / self.step_x
		case_y = y/self.step_y 
		self.tab_proba[ case_x-1 , case_y-1 ] = proba

	def test_remplir( self ) :
          
          for i in range( self.nb_x ):
              for j in range( self.nb_y ):
                   x = i * self.step_x
                   y = j * self.step_y
                   self.set_proba( 1, x, y  )
                   self.set_norm( 1, x, y  )
                   
"""data = discretedata()
data.test_remplir()
print data.tab_proba
print data.tab_norm"""
    
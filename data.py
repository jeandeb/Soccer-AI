import numpy



class data_passe( object ) : 

	def __init__( self, nb_x, nb_y, nb_var ) : 

		self.nb_y = nb_y
		self.nb_x = nb_x
		self.nb_var = nb_var
		self.state =  np.zeros( self.nb_x, self.nb_y, self.nb_var )


class data_tir( object ) : 

	def __init__( self, nb_x, nb_y ) :

		self.nb_y = nb_y
		self.nb_x = nb_x
		self.state = np.zeros( self.nb_x, self.nb_y )





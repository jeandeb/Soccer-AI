import numpy



class data( object ) : 

	def __init__( self, nb_gen, nb_var ) : 

		self.nb_gen = nb_gen
		self.nb_var = nb_var
		self.state =  np.zeros( self.nb_gen, self.nb_var )
		self.cpt = 0

	def calcul_proba( boole, nb_essai )


		if cpt >= nb_essai : 
			cpt = 0

		if boole : 
			cpt += 1


class data_tir( object ) : 

	def __init__( self, nb_x, nb_y ) :

		self.nb_y = nb_y
		self.nb_x = nb_x
		self.state = np.zeros( self.nb_x, self.nb_y )





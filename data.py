
import numpy as np

class data( object ) : 

	def __init__( self, nb_gen, nb_essai, nb_var ) : 

		self.nb_gen = nb_gen
		self.nb_var = nb_var
		self.nb_essai = nb_essai
		self.state =  np.zeros(( self.nb_gen, self.nb_var, self.nb_essai, 3 ))
		self.cpt = 0.0
		self.success = 0.0

	def calcul_proba( self, boole, norm, angle, step ) : 

		#print step, self.cpt, self.success
		if step == 0 :
			return

		num_gen = step//(self.nb_essai*self.nb_essai*2)

		#temporaire
		essai = step%self.nb_essai
		if (essai == 0 ): 
			self.state[num_gen-1][0] = norm
			self.state[num_gen-1][1] = angle
			self.state[num_gen-1][2][self.nb_essai-1][2] = self.success/(step-1)%self.nb_essai
			self.success = 0

		elif boole : 
			self.success += 1

	def set_essai( self, vecteur, step ):

			num_gen = step//(self.nb_essai*self.nb_essai*2)
			essai = step%self.nb_essai
			self.state[num_gen-1][2][self.nb_essai-1][0] = vecteur.norm
			self.state[num_gen-1][2][self.nb_essai-1][1] = vecteur.angle

class data_dicho( object ) : 

	def __init__( self, nb_essai, nb_dicho ) : 


		self.nb_essai = nb_essai
		self.nb_dicho = nb_dicho
		self.state =  np.zeros(( self.nb_essai*self.nb_dicho, 3 ))
		self.cpt = 0.0
		self.success = 0.0

	def calcul_proba( self, boole, nb_tirs ) : 

		#print step, self.cpt, self.success
		if boole : 
			self.success += 1.

		pos = nb_tirs//(self.nb_essai*2)
		essai = nb_tirs%(self.nb_essai*2)
		if ( essai >= 2*self.nb_essai-1 ): 
			#print "success = " + str( self.success )
			#print " essai " + str(nb_tirs%self.nb_essai+1)
			self.state[pos][2] = self.success/(nb_tirs%self.nb_essai+1)
			self.success = 0.


	def set_essai( self, vecteur, nb_tirs ):

			pos = nb_tirs//(self.nb_essai*2)

			self.state[pos][1] = vecteur.norm
			self.state[pos][0] = vecteur.angle

	def to_zero( self ):

		for i in self.state : 
			i = [0.,0.,0.]

		self.cpt = 0.
		self.success = 0.


class data_rand( object ) : 

	def __init__( self, nb_rand, nb_essai ) : 


		self.nb_essai = nb_essai
		self.nb_rand = nb_rand
		self.state =  np.zeros(( self.nb_rand, 4 ))
		self.cpt = 0.0
		self.success = 0.0

	def calcul_proba( self, boole, nb_tirs ) : 

		if boole : 
			self.success += 1.

		nb_tirs = nb_tirs//2

		pos = (nb_tirs)//(self.nb_essai)
		essai = nb_tirs%(self.nb_essai) + 1
		if ( essai == self.nb_essai ): 
			
			self.state[pos][2] = self.success/(essai)
			self.success = 0.

	def set_essai( self, vecteur, nb_tirs ):

			pos = nb_tirs//(self.nb_essai*2)

			self.state[pos][1] = vecteur.norm
			self.state[pos][0] = vecteur.angle

	def to_zero( self ):

		for i in self.state : 
			i = [0.,0.,0.]

		self.cpt = 0.
		self.success = 0.

	def set_score( self, score, nb_tirs ):

		pos = nb_tirs//(self.nb_essai*2)
		essai = nb_tirs%(self.nb_essai*2)

		self.state[pos][3] += score


class data_gen( object ) : 

	def __init__( self, nb_rand, nb_essai ) : 


		self.nb_essai = nb_essai
		self.nb_rand = nb_rand
		self.state =  np.zeros(( self.nb_rand, 6 ))
		self.cpt = 0.0
		self.success = 0.0

	def calcul_proba( self, boole, nb_action ) : 

		if boole : 
			self.success += 1.

		nb_action = nb_action//2

		pos = (nb_action)//(self.nb_essai)
		essai = nb_action%(self.nb_essai) + 1
		if ( essai == self.nb_essai ): 
			
			self.state[pos][4] = self.success/(essai)
			self.success = 0.

	def set_essai( self, vitesse, tir, nb_action ):

			pos = nb_action//(self.nb_essai*2)

			self.state[pos][0] = vitesse.angle
			self.state[pos][1] = vitesse.norm

			self.state[pos][2] = tir.angle
			self.state[pos][3] = tir.norm

	def to_zero( self ):

		for i in self.state : 
			i = [0.,0.,0.,0.,0.,0.]

		self.cpt = 0.
		self.success = 0.

	def set_score( self, score, nb_tirs ):

		pos = nb_tirs//(self.nb_essai*2)
		essai = nb_tirs%(self.nb_essai*2)

		self.state[pos][5] += score








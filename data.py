
import numpy as np

class data( object ) : 

	def __init__( self, nb_gen, nb_essai, nb_var ) : 

		self.nb_gen = nb_gen
		self.nb_var = nb_var
		self.nb_essai = nb_essai
		self.state =  np.zeros(( self.nb_gen, self.nb_var, self.nb_essai ))
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
			self.state[num_gen-1][2][self.nb_essai-1] = self.success/(step-1)%self.nb_essai
			self.success = 0

		elif boole : 
			self.success += 1

			


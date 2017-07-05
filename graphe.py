import matplotlib.pyplot as plt
import pickle
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import sys
import protodicho
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
data = None

if( (len(sys.argv) > 1) ) :
	nom = sys.argv[1]
	data = pickle.load( open( "pickle_files/" + nom, "rb" ) )



PREC = 0.8
NB_ESSAI = 20
NB_DICHO = 20
#proba = np.zeros(( len( data ) ))
angle = []
norm = []
proba = []

for i in range( len( data ) ) : 
		angle.append(data[i][0])
		norm.append(data[i][1])
		proba.append( data[i][2] )


plt.xlabel('Angles (rad)')
plt.ylabel( 'Normes' )
plt.scatter( angle, norm, s=5, alpha=1, c=proba)
plt.title( 'Proba de tirer en fonction de langle et de la norme' )
plt.legend()
plt.show()




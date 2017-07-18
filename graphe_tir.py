import matplotlib.pyplot as plt
import pickle
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import sys
import protodicho
import math
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
data = None

if( (len(sys.argv) > 1) ) :
	nom = sys.argv[1]
	data = pickle.load( open( "pickle_files/" + nom, "rb" ) )



#proba = np.zeros(( len( data ) ))
x = []
y = []
proba = []

print data
for i in range( len( data ) ) : 
		x.append(data[i][2][0])
		y.append(data[i][2][1])
		proba.append( data[i][5][1])
		print " X = " + str(data[i][2][0]) + " Y = " + str(data[i][2][1]) + " Proba = " + str(data[i][6][0]) + " Norme = " + str(data[i][5][1]) + "Angle = " + str(data[i][5][0])


plt.xlabel('X')
plt.ylabel( 'Y' )
plt.scatter( x, y, s=5, alpha=1, c=proba)
plt.title( 'Proba de tirer en fonction de la position du joueur' )
plt.legend()
plt.show()
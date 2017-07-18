from sklearn import linear_model
import numpy as np
import math
import sys
import pickle
import matplotlib.pyplot as plt
from soccersimulator.utils import Vector2D

model = linear_model.LinearRegression( n_jobs=-1 )

print 1

if( (len(sys.argv) > 1) ) :
	nom = sys.argv[1]
	data = pickle.load( open( "pickle_files/" + nom, "rb" ) )



print 2

n_sample = len( data )
features = np.zeros(( n_sample, 1 ))
target = np.zeros(( n_sample, 1 ))
weight = np.zeros(( n_sample ))
error = np.zeros(( n_sample ))
tab = []

for i in range( n_sample ) :

	vecteur = Vector2D( data[i][2][0], data[i][2][1])
	#features[i][0] = data[i][0][0]
	features[i][0] = data[i][0][1]

	target[i][0] = data[i][5][1]
	

	#weight[i] = 1 + data[i][6][0]

model.fit( features, target )

for i in range( n_sample ) :
	vecteur = Vector2D( data[i][2][0], data[i][2][1] )
	tab.append([data[i][0][1]])

print tab
valeur = model.predict( tab )
print valeur
x = []
y = []
proba = []

for i in range( n_sample ) : 
		x.append( data[i][2][0] )
		y.append( data[i][2][1] )
		proba.append( valeur[i][0] )
		print " X = " + str(data[i][2][0]) + " Y = " + str(data[i][2][1]) + " Proba = " + str(valeur[i][0]) 

plt.xlabel('X')
plt.ylabel( 'Y' )
plt.scatter( x, y, s=5, alpha=1, c=proba)
plt.title( 'Proba de tirer en fonction de la position du joueur' )
plt.legend()
plt.show()

#print 4

pickle.dump( model, open( "Regression_model/" + sys.argv[1], "wb" ) )
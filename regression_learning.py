from sklearn import linear_model
import numpy as np
import math
import sys
import pickle
import matplotlib.pyplot as plt
from soccersimulator.utils import Vector2D

def error_tab( tab_val, tab_target ):
	tab_error = [0.,0.,0.,0.]

	for i in range( len( tab_error ) ) :
		if( tab_target[i] == 0 ) : 
			continue
		tab_error[i] = math.fabs( tab_target[i]-tab_val[i] )/tab_target[i]	

	return tab_error

def error_val( tab_error ):
	val = 0
	for i in tab_error:
		val += i
	return math.pow( val, 2 )



model = linear_model.LinearRegression( n_jobs=-1 )

if( (len(sys.argv) > 1) ) :
	nom = sys.argv[1]
	data = pickle.load( open( "pickle_files/" + nom, "rb" ) )


n_sample = 50
n_test = len( data ) - n_sample

features = np.zeros(( n_sample, 2 ))
target = np.zeros(( n_sample, 5 ))
weight = np.zeros(( n_sample ))

test_features = np.zeros(( n_test, 2 ))
test_target = np.zeros(( n_test, 5 ))

error = np.zeros(( n_sample ))
test_error = np.zeros(( n_test ))



#TABLEAUX FEATURES, TARGET, FIT DU MODELE
#---------------------------------

for i in range( n_sample ) :

	vec = Vector2D( angle=data[i][0][0], norm=data[i][0][1] ) + Vector2D( angle=data[i][1][0], norm=data[i][1][1] )
	features[i][0] = vec.angle
	features[i][1] = vec.norm
	#features[i][2] = data[i][1][0]
	#features[i][3] = data[i][1][1]
	#features[i][4] = data[i][0][0]*data[i][0][0]
	#features[i][5] = data[i][0][1]*data[i][0][1]
	#features[i][6] = data[i][0][1]*data[i][0][0]

	target[i][0] = data[i][4][0]
	target[i][1] = data[i][4][1]
	target[i][2] = data[i][5][0]
	target[i][3] = data[i][5][1]
	target[i][4] = data[i][6][0]
	

	weight[i] = data[i][6][0]*2

model.fit( features, target, weight )

#TABLEAUX DE TESTS
#---------------------------------
for i in range( n_sample, n_sample + n_test ) : 
	vec = Vector2D( angle=data[i][0][0], norm=data[i][0][1] ) + Vector2D( angle=data[i][1][0], norm=data[i][1][1] )
	test_features[i-n_sample][0] = vec.angle
	test_features[i-n_sample][1] = vec.angle 
	#test_features[i-n_sample][2] =  data[i][1][0]
	#test_features[i-n_sample][3] =  data[i][1][1]
	#test_features[i-n_sample][4] = data[i][0][0]*data[i][0][0]
	#test_features[i-n_sample][5] = data[i][0][1]*data[i][0][1]
	#test_features[i-n_sample][6] = data[i][0][1]*data[i][0][0]

	test_target[i-n_sample][0] = data[i][4][0]
	test_target[i-n_sample][1] = data[i][4][1]
	test_target[i-n_sample][2] = data[i][5][0]
	test_target[i-n_sample][3] = data[i][5][1]


#print test_set
valeur = model.predict( features )
valeurs_test = model.predict( test_features )


#CALCUL ERREUR / LOSS FUNCTION
#---------------------------------
tot_test_error = 0
tot_error = 0

for i in range( n_test ) :
	test_error[i] = error_val( error_tab( valeurs_test[i], test_target[i] ) )
	tot_test_error += test_error[i]

for i in range( n_sample ):
	error[i] = error_val( error_tab( valeur[i], target[i] ) )
	tot_error += error[i]

print tot_error
print tot_test_error
tot_test_error = tot_test_error/n_test
tot_error = tot_error/n_sample



print "ERROR TOTAL = " + str(tot_error)
print "TEST TOTAL = " + str( tot_test_error )

#AFFICHAGE GRAPHE
#---------------------------------
x = []
y = []
angle = []
norm = []

#Tableaux pour affichage
for i in range( n_sample ) : 
		x.append( data[i][0][0] )
		y.append( data[i][0][1] )
		angle.append( valeur[i][2] )
		norm.append( valeur[i][3] )
		#print " X = " + str(data[i][2][0]) + " //Y = " + str(data[i][2][1]) + " //ANGLE = " + str(valeur[i][2]) + " //NORM = "+ str(valeur[i][3]) 

plt.xlabel('angle')
plt.ylabel( 'distance' )
plt.scatter( x, y, s=5, alpha=1, c=angle)
plt.title( 'Predictions ANGLE' )
plt.legend()
#plt.show()

plt.xlabel('angle')
plt.ylabel( 'distance' )
plt.scatter( x, y, s=5, alpha=1, c=norm)
plt.title( 'Predictions NORME' )
plt.legend()
#plt.show()



#SAVEMODEL
#---------------------------------
pickle.dump( model, open( "Regression_model/" + sys.argv[1], "wb" ) )







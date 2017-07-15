from sklearn import linear_model
import numpy as np
import math
import sys
import pickle

model = linear_model.LinearRegression( n_jobs=-1 )

print 1

if( (len(sys.argv) > 1) ) :
	nom = sys.argv[1]
	data = pickle.load( open( "pickle_files/" + nom, "rb" ) )



print 2

n_sample = len( data )
features = np.zeros(( n_sample, 2 ))
target = np.zeros(( n_sample, 1 ))
weight = np.zeros(( n_sample ))
error = np.zeros(( n_sample ))

for i in range( n_sample ) :
	#features[i][0] = data[i][0][0]
	#features[i][1] = data[i][0][1]
	#features[i][2] = data[i][1][0]
	#features[i][3] = data[i][1][1]
	#features[i][4] = data[i][2][0]
	#features[i][5] = data[i][2][1]
	features[i][0] = data[i][2][0]
	features[i][1] = data[i][2][1]
	#features[i][8] = data[i][7][0] 
	#features[i][8] = data[i][7][1] 

	#target[i][0] = data[i][5][0]
	#target[i][1] = data[i][5][1]
	target[i][0] = data[i][6][0]
	

	#weight[i] = 1 + data[i][6][0]

#print 3

model.fit( features, target )
print "data = " + str(data[5])
print "target = " + str(target[5])
#tab = [data[5][0][0], data[5][0][1], data[5][1][0], data[5][1][1], data[5][2][0], data[5][2][1], data[5][3][0], data[5][3][1], data[5][7][0], data[5][7][1]]
tab = [data[2][2][0],data[2][2][1]]
print "tab = " + str(tab)
valeur = model.predict( [tab] )
print "valeur = " + str(valeur)
for i in 


#print 4

pickle.dump( model, open( "Regression_model/" + sys.argv[1], "wb" ) )
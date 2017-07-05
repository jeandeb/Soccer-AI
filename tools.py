import data
import random
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import math
import numpy as np 

NB_GENER = 100
GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10

      
    
class StaticStrategy(Strategy):
    def __init__(self):
        super(StaticStrategy,self).__init__("Static")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction()

class PasseLearningStrat( Strategy ) : 
    def __init__(self,shoot=None):
        self.name = "simple action"
        self.passe = Vector2D()
        self.vitesse = Vector2D()
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(self.vitesse,self.passe)




def init_game( strat, goal=None ) : 

	team1 = SoccerTeam( "Joueurs" )
	team1.add( "Passeur", strat[0] )

	if ( len( strat ) > 1 ) : 
		team1.add( "Receveur", strat[1] )

	if( goal ) : 
		team2 = SoccerTeam( "Goal" )
		team2.add( "Goal", goal )
	else :
		team2 = SoccerTeam( "Static" )
		team2.add( "Static", Strategy() )

	simu = Simulation( team1, team2, max_steps=100000000 )

	return simu

def generator( nb_j, simu ) : 


	x_rand1 = random.randint( 1, GAME_WIDTH )
	y_rand1 = random.randint( 1, GAME_HEIGHT )
	position = Vector2D( x_rand1, y_rand1 )   
	simu.state.states[(1,0)].position = position.copy()
	simu.state.states[(1,0)].vitesse = Vector2D() 
	simu.state.ball.position = position.copy()
	

	if( nb_j > 1 ):
		x_rand2 = random.randint( 1, GAME_WIDTH )
		y_rand2 = random.randint( 1, GAME_HEIGHT )
		position2 = Vector2D( x_rand2, y_rand2 )  
		simu.state.states[(1,1)].position = position2.copy()
		x_rand2 = random.randrange( -10, 10 )
		y_rand2 = random.randrange( -10, 10 )
		vitesse = Vector2D( x_rand2, y_rand2 )
		simu.state.states[(1,1)].vitesse = vitesse
		return [position, position2, vitesse ]


	return [ position ]


def positionne( liste, simu ):
	
	simu.state.states[(1,0)].position = liste[0].copy()
	simu.state.states[(1,0)].vitesse = Vector2D() 
	simu.state.ball.position = liste[0].copy()

	if( len(liste) > 2 ): 
		simu.state.states[(1,1)].position = liste[1]
		simu.state.states[(1,1)].vitesse = liste[2]

def shoot_rand( dicho ) : 

	#print dicho
	angle1 = dicho[0][0]
	norm1 = dicho[0][1]
	angle2 = dicho[1][0]
	norm2 = dicho[1][1]

	norm = np.random.normal(loc=0., scale=1 )
	angle = np.random.normal(loc=0., scale=0.2 )
	#print norm
	#print angle

	if( norm1 >= norm2 ) : 
		norm += norm2 + ( norm2 - norm1 ) * random.random()
	else : 
		norm += norm1 + ( norm1 - norm2 ) * random.random()

	if( angle1 >= angle2 ) : 
		angle += angle2 + ( angle1 - angle2 ) * random.random()
	else : 
		angle += angle1 + ( angle2 - angle1 ) * random.random()

	return Vector2D( angle = angle, norm = norm )

def best_two( tab, dicho ):

	print tab
	print dicho
	for i in tab : 
		if( dicho[0][0] == i[0] and dicho[0][1] == i[1] ) : 
			continue
		if (i[2] > dicho[0][2] ):
			dicho[0][0] = i[0]
			dicho[0][1] = i[1]
			dicho[0][2] = i[2]
		elif (i[2] > dicho[1][2] ) : 
			dicho[1][0] = i[0]
			dicho[1][1] = i[1]
			dicho[1][2] = i[2]

def swap( j, rmp ) : 
	j[0] = rmp[0]
	j[1] = rmp[1]
	j[2] = rmp[2]
	j[3] = rmp[3]

def best( tab, dicho ):

	#print tab
	#print dicho
	for i in tab : 
		if not (i.any()) :
			continue
		if (i[2] > dicho[2] ):
			swap( dicho, i )
		elif ((i[2] == dicho[2] ) and (i[3] < dicho[3]) ) : 
			swap( dicho, i )
		elif( i[2] == dicho[2] and i[2] != 0 and i[1] > dicho[1] ) : 
			swap( dicho, i )

def swap_best( tab, best ):

	if ( tab[2] > best[2] ):
		swap( best, tab )
	elif( tab[2] == best[2] and tab[2] != 0 and tab[1] > best[1] ) : 
		swap( best, tab )
	elif ((tab[2] == best[2] ) and (tab[3] < best[3])) : 
		swap( best, tab )	


def shoot_vect_rand( pos ):

	direc = dir( pos )

	angle = direc.angle
	norm = direc.norm

	angle_rand = angle + (math.pi/4)*random.random() - math.pi/8.
	norm_rand = 6*random.random()

	return Vector2D( angle = angle_rand, norm = norm_rand )

def dir( pos ) : 

	direction = Vector2D( GAME_WIDTH, GAME_HEIGHT/2. ) - pos[0]

	if len(pos) > 1 : 
		direction = pos[1] - pos[0]

	return direction


def valide( state, pos ) : 

	pos_balle = state.ball.position
	position = Vector2D( GAME_WIDTH, GAME_HEIGHT/2. )

	if len(pos) > 1 : 
		position = state.states[(1,1)].position
		return ((pos_balle - position).norm < 20) and (state.ball.vitesse.norm < 2)

	return (pos_balle.x > GAME_WIDTH) and (pos_balle.y >GAME_HEIGHT/2- GAME_GOAL_HEIGHT/2) and (pos_balle.y < GAME_HEIGHT/2 + GAME_GOAL_HEIGHT/2)



def valide_tir( state ) : 
	pos_balle = state.ball.position
	return (pos_balle.x > GAME_WIDTH) and (pos_balle.y >GAME_HEIGHT/2- GAME_GOAL_HEIGHT/2) and (pos_balle.y < GAME_HEIGHT/2 + GAME_GOAL_HEIGHT/2)

def score( state ) : 
	pos_balle = state.ball.position
	score = (Vector2D( GAME_WIDTH, GAME_HEIGHT/2 ) - pos_balle).norm

	return score

def valide_passe( state ) :
	pos_balle = state.ball.position
	position = state.states[(1,1)].position
	return ((pos_balle - position).norm < 6) and (state.ball.vitesse.norm < 1)

def shoot_rand_search( tab ):

	angle = 2*math.pi*random.random()
	norm = random.random()*8
	tab[0] = angle
	tab[1] = norm

	return Vector2D( angle=angle, norm=norm )


def new_shoot( elem ) : 

	a_scale = 0.5
	n_scale = 1.5

	a_x = np.random.normal(loc=elem[0], scale=a_scale )
	n_x = np.random.normal(loc=elem[1], scale=n_scale )
	#print "angle = "+ str(a_x)


	return Vector2D( angle = a_x, norm = n_x )








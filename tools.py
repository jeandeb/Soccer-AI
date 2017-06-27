import data
import random
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import math

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
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D(),self.passe)


def init_game( strat ) : 

	team1 = SoccerTeam( "Joueurs" )
	team1.add( "Passeur", strat[0] )

	if ( len( strat ) > 1 ) : 
		team1.add( "Receveur", strat[1] )

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


def shoot_vect_rand( pos ):

	direc = dir( pos )

	angle = direc.angle
	norm = direc.norm

	angle_rand = angle + (math.pi/4)*random.random() - math.pi/8.
	norm_rand = 8*random.random()

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

















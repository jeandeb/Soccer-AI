import data
import random
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import math
from Projet_2I013 import strategy
import tools
import Projet_2I013
import numpy as np

NB_GENER = 100
GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10

class LearningStrat( Strategy ) : 
    def __init__(self,shoot=None):
        self.name = "simple action"
        self.passe = Vector2D()
        self.vitesse = Vector2D()
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(self.vitesse,self.passe)

class StaticStrategy(Strategy):
    def __init__(self):
        super(StaticStrategy,self).__init__("Static")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction()

class IntercepteStrategy(Strategy):
    def __init__(self):
        self.name = "Intercepte"
    def compute_strategy(self,state,id_team,id_player):
    	prop =  Projet_2I013.tools.properties(state,id_team,id_player )
        basic_action = Projet_2I013.tools.basic_action(prop )

        return basic_action.go_ball + basic_action.shoot_goal_max

class DribbleStrat( Strategy ) : 
    def __init__(self,shoot=None):
        self.name = "Dribble"
        self.passe = Vector2D()
        self.vitesse = Vector2D()
    def compute_strategy(self,state,id_team,id_player):

    	prop =  Projet_2I013.tools.properties(state,id_team,id_player )
        basic_action = Projet_2I013.tools.basic_action(prop )

        return SoccerAction(self.vitesse,self.passe) + basic_action.go_ball 

class ConduireStrat( Strategy ) : 
    def __init__(self,shoot=None):
        self.name = "Conduire"
        self.passe = Vector2D()
        self.vitesse = Vector2D()
    def compute_strategy(self,state,id_team,id_player):

    	prop =  Projet_2I013.tools.properties(state,id_team,id_player )
        basic_action = Projet_2I013.tools.basic_action(prop )

        return SoccerAction(self.vitesse,self.passe) + basic_action.go_ball 



def init_game( strateq, stratad) : 

	cpt = 0
	team1 = SoccerTeam( "IA" )

	for i in strateq : 
		cpt += 1
		team1.add( "J" + str(cpt), i )

	cpt = 0

	team2 = SoccerTeam( "AD" )

	for i in stratad : 

		cpt += 1
		team2.add( "A" + str(cpt), i )

	simu = Simulation( team1, team2, max_steps=100000000 )

	return simu

def random_position():
	x = random.randint( 0, GAME_WIDTH )
	y = random.randint( 0, GAME_HEIGHT )
	position = Vector2D( x, y ) 
	return position

def random_vitesse():
	x = random.randrange( -3, 3 )
	y = random.randrange( -3, 3 )
	vitesse = Vector2D( x, y )
	return vitesse

def random_pos_vit( simu, equipe, joueur ) : 

	position = random_position()
	simu.state.states[(equipe,joueur)].position = position

	vitesse = random_vitesse()
	simu.state.states[(equipe,joueur)].vitesse = vitesse

	return position, vitesse


def generator(  action, strateq, stratad, simu ):

	#position aleatoire j1
	position, vitesse = random_pos_vit( simu, 1, 0 )
	if action[0] == "Dribble" or action[0] == "Conduire" :
			position = Vector2D(75,45)

	if action[0] == "Conduire" :
			vitesse = Vector2D()


	tab = [[position, vitesse ]]

	#pos/vit balle alea ? 
	if action[1][0] : 
	
		position_b = random_position()
		simu.state.ball.position = position_b



		vitesse = random_vitesse()
		simu.state.ball.vitesse = vitesse

	else :
		position_b = position
		simu.state.ball.position = position_b

		vitesse = Vector2D()
		simu.state.ball.vitesse = vitesse

	tab.append( [position_b, vitesse ])
	

	if len( strateq ) > 1 and action[1][1] :

		position2, vitesse = random_pos_vit( simu, 1, 1 )
		if action[0] == "Conduire" :
			vitesse = Vector2D()

		tab.append( [position2, vitesse, 1] )

	elif action[1][1] : 
		if( stratad[0].name ==  "Goal" ) :
			simu.state.states[(2,0)].position = Vector2D( 140, 45 )
		else :

			position3, vitesse = random_pos_vit( simu, 2, 0 )

			if action[0] == "Degage" :
				while (position3 - position).x <= 0 or  (position3 - position).norm >= 60 : 
					position3, vitesse = random_pos_vit( simu, 2, 0 )
					vitesse = Vector2D()
			elif action[0] == "Dribble" :
				while (position3 - position).x <= 0  or  (position3 - position).norm >= 40 : 
					position3, vitesse = random_pos_vit( simu, 2, 0 )
					vitesse = Vector2D()
			elif action[0] == "Conduire" : 
				position3 = position + Vector2D( -4, 0 )
				vitesse = Vector2D()

			tab.append( [position3, vitesse, 2] )

	return tab



def positionne( liste, simu ):
	
	simu.state.states[(1,0)].position = liste[0][0]
	simu.state.states[(1,0)].vitesse = liste[0][1]

	simu.state.ball.position = liste[1][0]
	simu.state.ball.vitesse = liste[1][1]


	if( len(liste) > 2 ): 
		simu.state.states[(liste[2][2],2-liste[2][2])].position = liste[2][0]
		simu.state.states[(liste[2][2],2-liste[2][2])].vitesse = liste[2][1]

def new_vitesse( elem ) : 

	a_scale = 0.1 + (1 - elem[2])/2
	n_scale = 0.01 + (1 - elem[2])/100
	if n_scale < 0 : 
		n_scale = -n_scale

	a_x = np.random.normal(loc=elem[0], scale=a_scale )
	n_x = np.random.normal(loc=elem[1], scale=n_scale )
	#print "angle = "+ str(a_x)

	#print Vector2D( angle = a_x, norm = n_x ).norm
	return Vector2D( angle = a_x, norm = n_x )

def generator_action( dicho, action, strat, state ) : 

	if action[2][0]:
		elem = [dicho[0][0], dicho[0][1], dicho[2][0]]
		strat.vitesse = new_vitesse( elem )


	if action[2][1]:
		elem = [dicho[1][0], dicho[1][1], dicho[2][0]]
		strat.passe = tools.new_shoot( elem )


def best_elem( elem, dicho ) :

	if (elem[4] > dicho[2][0] ):
		swap( dicho, elem )
	elif ((elem[4] == dicho[2][0] ) and (elem[5] < dicho[2][1]) ) : 
		swap( dicho, elem )

def swap( dicho, elem ) : 

	dicho[0][0] = elem[0]
	dicho[0][1] = elem[1]
	dicho[1][0] = elem[2]
	dicho[1][1] = elem[3]
	dicho[2][0] = elem[4]
	dicho[2][1] = elem[5]



def set_data_alea(  data_alea, dicho, action, pos, num_etat ) : 

	pos_ad_joueur = Vector2D()
	vit_ad = Vector2D()

	if( action[1][0] ) : 
		pos_ad_joueur = pos[1][0] - pos[0][0]
		vit_ad = pos[1][1]
	elif action[1][1] : 
		pos_ad_joueur = pos[2][0] - pos[0][0]
		vit_ad = pos[2][1]
	else : 
		pos_ad_joueur = Vector2D( GAME_WIDTH, GAME_HEIGHT/2 ) - pos[0][0]

	data_alea[num_etat][0][0] = pos_ad_joueur.angle
	data_alea[num_etat][0][1] = pos_ad_joueur.norm

	data_alea[num_etat][1][0] = vit_ad.angle
	data_alea[num_etat][1][1] = vit_ad.norm

	data_alea[num_etat][2][0] = pos[0][0].x
	data_alea[num_etat][2][1] = pos[0][0].y

	data_alea[num_etat][3][0] = pos[0][1].angle
	data_alea[num_etat][3][1] = pos[0][1].norm

	data_alea[num_etat][4][0] = dicho[0][0]
	data_alea[num_etat][4][1] = dicho[0][1]

	data_alea[num_etat][5][0] = dicho[1][0]
	data_alea[num_etat][5][1] = dicho[1][1]

	data_alea[num_etat][6][0] = dicho[2][0]
	data_alea[num_etat][6][1] = dicho[2][1]

	vecteur_direction = pos_ad_joueur + vit_ad
	data_alea[num_etat][7][0] = vecteur_direction.norm
	data_alea[num_etat][7][1] = vecteur_direction.angle




#(Vecadjoueur, Vitadouballe, Posjoueur, Vitjoueur, Vit, Tir, Proba)
#self.data_alea, self.dicho, self.action, self.pos, num_etat


def valide( state, action ) : 

	if( action[0] == 'Tir' ):
		return tools.valide_tir( state )

	elif( action[0] == 'Passe' ):
		return valide_passe( state )

	elif( action[0] == 'Dribble' ):
		return valide_dribble( state )

	elif( action[0] == 'Intercepte' ):
		return valide_intercepte( state )

	elif( action[0] == 'Conduire' ):
		return valide_conduire( state )

	elif( action[0] == 'Degage' ):
		return valide_degage( state )

def valide_passe( state ):

	pos_balle = state.ball.position
	position = state.states[(1,1)].position
	return ((pos_balle - position).norm < 5) and (state.ball.vitesse.norm < 0.1)

def valide_dribble( state ):

	pos_balle = state.ball.position
	position_ad = state.states[(2,0)].position
	position = state.states[(1,0)].position

	return (pos_balle - position_ad).x > 5 and (pos_balle - position).norm < 2

def valide_intercepte( state ): 

	pos_balle = state.ball.position
	position = state.states[(1,0)].position

	return ((pos_balle - position).norm < 2)

def valide_conduire( state ): 
	pos_balle = state.ball.position
	position = state.states[(1,1)].position
	if (pos_balle - position).norm < 1 : 
		print "TRUUUUE"
	return (pos_balle - position).norm < 1

def valide_degage( state ): 

	pos_balle = state.ball.position
	position = state.states[(2,0)].position

	return ((pos_balle - position).x > 4) and ((pos_balle - position).norm > 6)


def score( state, action ) : 

	if( action[0] == 'Tir' ):
		return tools.score( state )

	elif( action[0] == 'Passe' ):
		return score_passe( state )

	elif( action[0] == 'Dribble' ):
		return score_dribble( state )

	elif( action[0] == 'Intercepte' ):
		return score_intercepte( state )

	elif( action[0] == 'Conduire' ):
		return score_conduire( state )

	elif( action[0] == 'Degage' ):
		return score_degage( state )

def score_passe( state ):

	pos_balle = state.ball.position
	position = state.states[(1,1)].position

	return (pos_balle - position).norm

def score_dribble( state ):
	pos_balle = state.ball.position
	position = state.states[(2,0)].position

	return (pos_balle - position).x

def score_intercepte( state ): 
	pos_balle = state.ball.position
	position = state.states[(1,0)].position

	return (pos_balle - position).norm 

def score_conduire( state ): 
	position_self = state.states[(1,0)].position
	position_obj = state.states[(1,1)].position
	pos_balle = state.ball.position
	return -(pos_balle - position_self).norm - (pos_balle - position_obj).norm

def score_degage( state ):

	pos_balle = state.ball.position
	position = state.states[(2,0)].position

	return (pos_balle - position).norm + state.ball.vitesse.norm*100








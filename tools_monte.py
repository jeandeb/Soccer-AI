import data
import random
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import math
from Projet_2I013 import strategy
from Projet_2I013 import tools as ts
import numpy as np
import tools_gen as tg
NB_GENER = 100
GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10

class MonteStrat( Strategy ) :

    def __init__(self):
        self.name = "Monte"
        self.action = SoccerAction( Vector2D(), Vector2D() )

    def compute_strategy(self,state,id_team,id_player):

        return self.action

def generator( state, simu ) :

	position_j1 = tg.random_position()
	simu.state.states[(1,0)].position = position_j1


	position_j2 = tg.random_position()	
	simu.state.states[(2,0)].position = position_j2

	alea = random.random()

	if alea <= 0.5 : 
		simu.state.ball.position = position_j1
		simu.state.ball.vitesse = tg.random_vitesse()
	else : 
		simu.state.ball.position = tg.random_position()



def set_state( simu ):

	state = [0,0,0,0,0]

	if simu.state.ball.position.y < 50 or simu.state.ball.position.y > 40 :

		if simu.state.ball.position.x > 150 : 
			state = [-1,-1,-1,-1,-1]
			return state
		elif simu.state.ball.position.x < 0 : 
			state = [-2,-2,-2,-2,-2] 
			return state

	pos_x = simu.state.ball.position.x//(GAME_WIDTH//5)
	pos_y = simu.state.ball.position.y//(GAME_HEIGHT//5)

	if pos_x > 4 : 
		pos_x = 4
	if pos_y > 4 : 
		pos_y = 4
	state[0] = int(pos_y * 5 + pos_x) 

	pos_x = simu.state.states[(1,0)].position.x//(GAME_WIDTH//5)
	pos_y = simu.state.states[(1,0)].position.y//(GAME_HEIGHT//5)

	if pos_x > 4 : 
		pos_x = 4
	if pos_y > 4 : 
		pos_y = 4
	state[1] = int(pos_y * 5 + pos_x) 

	pos_x = simu.state.states[(2,0)].position.x//(GAME_WIDTH//5)
	pos_y = simu.state.states[(2,0)].position.y//(GAME_HEIGHT//5)

	if pos_x > 4 : 
		pos_x = 4
	if pos_y > 4 : 
		pos_y = 4
	state[2] = int(pos_y * 5 + pos_x) 

	if state[0] == state[1] : 
		state[3] = 1

	if simu.state.ball.vitesse.x < 0 : 
		state[4] = 1

	return state

def set_returns( state, new_state, returns, q_tab, strat, new_strat ):

	#print "SET RETURNS"
	reward = rewards( state, new_state )

	reward += q_tab[new_state[0]][new_state[1]][new_state[2]][new_state[3]][new_state[4]][new_strat]

	nb_iter = returns[state[0]][state[1]][state[2]][state[3]][state[4]][strat][1]

	total = nb_iter*returns[state[0]][state[1]][state[2]][state[3]][state[4]][strat][0]
	total += reward

	returns[state[0]][state[1]][state[2]][state[3]][state[4]][strat][1] = nb_iter+1
	returns[state[0]][state[1]][state[2]][state[3]][state[4]][strat][0] = total/(nb_iter+1)
	#print returns[state[0]][state[1]][state[2]][state[3]][state[4]][strat]
	q_tab[state[0]][state[1]][state[2]][state[3]][state[4]][strat] = total/(nb_iter+1)


def rewards( state, new_state ):

	reward = 0
	if new_state[0] == -1 : 
		reward += 100
	elif new_state[0] == -2 :
		reward += -100
	elif (state[0] % 5) < (new_state[0] % 5):
		reward += -10
	elif (state[0] % 5) > (new_state[0] % 5):
		reward += 10
	else :
		reward += -1

	return reward

def best_strat( q_tab, new_state ):

	tab_action = q_tab[new_state[0]][new_state[1]][new_state[2]][new_state[3]][new_state[4]]
	maximum = 0
	i_max = 0

	for i in range( len(tab_action) ) : 
		if tab_action[i] >= maximum:
			maximum = tab_action[i]
			i_max = i

	if maximum == 0:
		i_max = int(random.randrange( 0, len(tab_action) ))

	return i_max


def set_strat( new_strat, strateq, state  ):
	#print "set_strat"
	prop =  ts.properties( state, 1 , 0 )

	basic_action = ts.basic_action(prop )
	#print 'new strat = ' + str( new_strat )
	if new_strat == 0 : 
		strateq[0].action = basic_action.aller_but

	elif new_strat == 1 :
		strateq[0].action = basic_action.shoot_learn

	elif new_strat == 2 :
		strateq[0].action = basic_action.dribble

	elif new_strat == 3 :
		strateq[0].action = basic_action.go_ball

	elif new_strat == 4 :
		strateq[0].action = basic_action.placement_def









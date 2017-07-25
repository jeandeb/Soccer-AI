import data
import random
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import math
from Projet_2I013 import strategy
import numpy as np
import tools_gen as tg



def generator( state, simu ) :

	position_j1 = tg.random_position()
	simu.state.states[(1,0)].position = position_j1


	position_j2 = tg.random_position()	
	simu.state.states[(2,0)].position = position_j2

	alea = math.random()

	if alea < 0.1 : 
		simu.state.ball.position = position_j2
		simu.state.ball.vitesse = tg.random_vitesse()
	else : 
		simu.state.ball.position = tg.random_position()



def set_state( simu ):

	state = [0,0,0,0,0]

	pos_x = simu.state.ball.position.x % 5
	pos_y = simu.state.ball.position.y % 5

	state[0] = pos_y * pos_x

	state = [0,0,0,0,0]

	pos_x = simu.state.states[(1,0)].position.x % 5
	pos_y = simu.state.states[(1,0)].position.y % 5

	state[1] = pos_y * pos_x

	state = [0,0,0,0,0]

	pos_x = simu.state.states[(2,0)].position.x % 5
	pos_y = simu.state.states[(2,0)].position.y % 5

	state[2] = pos_y * pos_x

	if state[0] == state[1] : 
		state[3] = 1

	if simu.state.ball.vitesse.x < 0 : 
		state[4] = 1

	return state

def set_returns( state, new_state, returns, q_tab, strat ):

	reward = rewards( state, new_state )

	reward += q_tab[new_state[0]][new_state[1]][new_state[2]][new_state[3]][new_state[4]][strat]
	nb_iter = returns[new_state[0]][new_state[1]][new_state[2]][new_state[3]][new_state[4]][strat][1]

	total = nb_iter*returns[new_state[0]][new_state[1]][new_state[2]][new_state[3]][new_state[4]][strat][0]
	total += reward

	returns[new_state[0]][new_state[1]][new_state[2]][new_state[3]][new_state[4]][strat][1] = nb_iter+1
	returns[new_state[0]][new_state[1]][new_state[2]][new_state[3]][new_state[4]][strat][0] = total/nb_iter+1

	q_tab[new_state[0]][new_state[1]][new_state[2]][new_state[3]][new_state[4]][strat] = total/nb_iter+1


def rewards( state, new_state ):

	if	












import data
import random
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
from Projet_2I013 import strategy_learning

NB_GENER = 100
GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain

def init_game( strat ) : 

	team1 = SoccerTeam( "Joueurs" )
	team1.add( "Passeur", strat[0] )

	if ( len( strat ) > 1 ) : 
		team1.add( "Receveur", strat[1] )

	team2 = SoccerTeam( "Static" )
	team2.add( "Static", Strategy() )

    simu = Simulation( team1, team2, max_steps=1000000 )
    simu.listeners += self

    return simu

def generator( strat, visu = True ) : 

	simu = init_game( strat )

	nb_j = len( strat )

	if visu :
		show_simu( simu )
    else:
		simu.start()

	data = data.data( self.nb_casex, self.nb_casey )

	for i in range( NB_GENER ) : 

		x_rand1 = random.randint( 1, GAME_WIDTH )
		y_rand1 = random.randint( 1, GAME_HEIGHT )
		position = Vector2D( x_rand1, y_rand1 )   
		simu.state.states[(1,0)].position = position.copy()
		simu.state.ball.position = position.copy()
        simu.state.states[(1,0)].vitesse = Vector2D() 

		if( nb_j > 1 ):
			x_rand2 = random.randint( 1, GAME_WIDTH )
			y_rand2 = random.randint( 1, GAME_HEIGHT )
			position = Vector2D( x_rand2, y_rand2 )  
			simu.state.states[(1,0)].position = position.copy()


	return











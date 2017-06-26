import data
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
from Projet_2I013 import strategy_learning
class RandomStrategy( Strategy ) : 
    def __init__( self ):

        Strategy.__init__( self, "Random" )
        self.vector2D = Vector2D.create_random( -1, 1 ) 

    def compute_strategy( self, state, id_team, id_player ):
  
        return SoccerAction( Vector2D(), self.vector2D )

def generator_passe( self, divfactor, nb_x, nb_y ) : 

	self.nb_casex = nb_x/divfactor
	self.nb_casey = nb_y/divfactor

	self.nb_var = 2 #pisition joueur1 et joueur2
	self.strat1 = strategy_learning.ShootingLearningStrat()
	self.strat2 = RandomStrategy()

	self.simu = init_game( self.nb_var, [self.strat1, self.strat2] )

	data = data.data( self.nb_casex, self.nb_casey )


	return

def init_game( self, nb_joueurs, strat ) : 

	team1 = SoccerTeam( "Joueurs" )
	team1.add( "Passeur", strat[0] )

	if ( nb_joueurs > 1 ) : 
		team1.add( "Receveur", strat[2] )

    simu = Simulation( team1, team2, max_steps=1000000 )
    simu.listeners += self

    return simu

def stop( ) : 

	return 


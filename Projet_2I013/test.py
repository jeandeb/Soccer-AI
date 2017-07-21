
import pickle

import strategy
#data_shoot = pickle.load( open( "tableau_learning/tab_shoot.p", "rb" ) )
#print data_shoot.tab_norm
## Creation d'une equipe
team1 = strategy.SoccerTeam( name = "AS FORBACH" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "MFC", login = "etu2" )

#team1.add( "Cavani", strategy.FonceurStrategy( ) ) 
#team2.add( "Defence", strategy.DefenceStrategy( ) )
#team1.add( "Sarko", strategy.StrikerStrategy( ) )
team2.add( "Sarko", strategy.DefenceStrategy( ) )
#team2.add( "Centre", strategy.CenterStrategy( ) )    
team2.add( "Hollande", strategy.StrikerStrategy( ) )
#team2.add( "Fillon", strategy.DefenceOffStrategy( ) )
#team2.add( "Striker", strategy.Striker4Strategy( ) )
#team2.add( "Aurier", strategy.SoloStrategy( ) )
#team2.add( "Barthez", strategy.StaticStrategy( ) )
#Creation d'une partie
#test4
#team1.add( "Striker", strategy.SoloStrategy( ) )
#team1.add( "Center", strategy.CenterStrategy( ) )
team1.add( "Defence", strategy.DefenceStrategy( ) )
#team1.add( "Defence", strategy.FonceurStrategy( ) )
#team1.add( "Barthez", strategy.GoalStrategy( ) )
#team1.add( "Defenseur", strategy.DefenceStrategy( ) ) 
team1.add( "Striker", strategy.StrikerStrategy( ) )
#team2.add( "Defence", strategy.DefenceStrategy( ) )
#team1.add( "Centre", strategy.CenterStrategy( ) )
simu = strategy.Simulation( team1, team2, max_steps=100000 )

#Jouer et afficher la partie
strategy.show_simu( simu )
#Jouer sans afficher
simu.start()
# -*- coding: utf-8 -*-<


from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
import strategy


def get_team( i ):
    MFC = SoccerTeam( name = "MFC"  )
    if i==1:
        MFC.add( "Cavani", strategy.SoloStrategy( ) ) 
    if i == 2 :
        MFC.add( "Yannis", strategy.DefenceStrategy( ) )
        MFC.add( "Cavani", strategy.StrikerStrategy( ) )
    if i == 4 :
        MFC.add( "Kipembe", strategy.DefenceStrategy( ) )
        MFC.add( "Cavani", strategy.Striker4Strategy( ) )
        MFC.add( "Barthez", strategy.GoalStrategy( ) )
        MFC.add( "Iniesta", strategy.CenterStrategy( ) )
    return MFC
    
    

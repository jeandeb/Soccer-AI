from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D
import logging
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import os.path
import strategy
import tools
import arbres




#team1 = SoccerTeam("forbach")
#strat_j1 = KeyboardStrategy()
#strat_j1.add('a',strategy.FonceurStrategy())
#strat_j1.add('z',strategy.DefPlacement())
#team1.add("Yannis",strat_j1)
#team1.add("Jexp 2",StaticStrategy())
#team2 = SoccerTeam("real_madrid")
#team2.add("Fonceur", strategy.FonceurStrategy())


def my_get_features(state,idt,idp):
    """ Choisir les elements qui vont rentrer en parametres dans les decisions de l'arbre """
    
    
    prop=tools.properties(state,idt,idp)
    f1=prop.dist_ball
    f2=prop.dist_goal
    f3=int(prop.near_play_ball)
    f4=prop.norm_min_ad
    return [f1,f2,f3,f4]


def entrainement(fn):

    simu = Simulation(team1,team2)
    show_simu(simu)
    # recuperation de tous les etats
    training_states = strat_j1.states
    # sauvegarde dans un fichier
    dump_jsonz(training_states,fn)
    
    
    
    
if __name__=="__main__":
    fn = "train_tree.jz"
    entrainement(fn)

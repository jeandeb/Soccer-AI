from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D
import logging
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree 	import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import os.path
import strategy
import tools
## Strategie aleatoire
class FonceStrategy(Strategy):
    def __init__(self):
        super(FonceStrategy,self).__init__("Fonce")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)

class StaticStrategy(Strategy):
    def __init__(self):
        super(StaticStrategy,self).__init__("Static")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction()

#######
## Constructioon des equipes
#######

#team1 = SoccerTeam("forbach")
#strat_j1 = KeyboardStrategy()
#strat_j1.add('x',strategy.AllerBut())
#strat_j1.add('c',strategy.GoBall())
#strat_j1.add('s',strategy.DefPlacement())
#strat_j1.add('d',strategy.Dribble())
#team1.add("Yannis",strat_j1)
#team1.add("Jexp 2",StaticStrategy())
team2 = SoccerTeam("real_madrid")
team2.add("Fonceur", FonceStrategy())
#team2.add("rien 2", StaticStrategy())



### Transformation d'un etat en features : state,idt,idp -> R^d
def my_get_features(state,idt,idp):
    """ extraction du vecteur de features d'un etat, ici distance a la balle, distance au but, distance balle but """
    
    prop = tools.properties(state,idt,idp)
    
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


def apprentissage(fn):
    ### chargement d'un fichier sauvegarder
    states_tuple = load_jsonz(fn)
    data_train, data_labels = build_apprentissage(states_tuple,my_get_features)
    dt = apprend_arbre(data_train,data_labels,depth=10)
    # Visualisation de l'arbre
    affiche_arbre(dt)
    genere_dot(dt,"test_arbre.dot")
    return dt


def jouer_arbre(dt):
    ####
    # Utilisation de l'arbre
    ###
    dic = {"Fonceur":strategy.FonceurStrategy(),"DefPlacement":strategy.DefPlacement(),"Static":strategy.StaticStrategy()}
    treeStrat1 = DTreeStrategy(dt,dic,my_get_features)
    team3 = SoccerTeam("Arbre Team")
    team3.add("Joueur 1",treeStrat1)
    simu = Simulation(team2,team3)
    show_simu(simu)

if __name__=="__main__":
    fn = "arbre_qui_marche/solo_arbre.jz"
    if not os.path.isfile(fn):
        entrainement(fn)
    dt = apprentissage(fn)
    jouer_arbre(dt)

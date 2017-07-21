from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D
import logging
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree 	import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import os.path
import strategy
import tools
import entrainement_arbre


my_get_features=entrainement_arbre.my_get_features



def apprentissage(fn):
    ### chargement d'un fichier sauvegarder
    states_tuple = load_jsonz(fn)
    ## Apprentissage de l'arbre
    data_train, data_labels = build_apprentissage(states_tuple,my_get_features)
    dt = apprend_arbre(data_train,data_labels,depth=10)
    # Visualisation de l'arbre
    affiche_arbre(dt)
    genere_dot(dt,"solo_arbre.dot")
    return dt

def jouer_arbre(dt):
    ####
    # Utilisation de l'arbre
    ###
    dic = {"Fonceur":strategy.FonceurStrategy(),"DefPlacement":strategy.DefPlacement(),"Static":strategy.StaticStrategy()}
    treeStrat1 = DTreeStrategy(dt,dic,my_get_features)

    team1 = SoccerTeam("Arbre Team")
    team1.add("Joueur 1",treeStrat1)
    team2 = SoccerTeam("real_madrid")
    team2.add("Fonceur", strategy.FonceurStrategy())
    
    simu = Simulation(team1,team2)
    show_simu(simu)
    
    
def solo_arbre():
    
    
if __name__=="__main__":
    fn = "train_tree.jz"
    if not os.path.isfile(fn):
        print('le fichier n\'est pas existant')
    dt = apprentissage(fn)
    jouer_arbre(dt)
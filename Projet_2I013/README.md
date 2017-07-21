# Projet_2I013
Projet SoccerSimulator

Machine Learning: 
13/02/2017 : 

  - Objectifs : 
Faire en sorte que chaque tir rentre dans les buts.

  - Conditions Initiales : 
Rayon de 50 par rapport a but
Distance par rapport a la balle
Angle de tir (90)

  - Variables :
dist_goal 
Angle 

  - Méthode Évaluation : 
Tir est rentré ou pas 

  - Paramètres à optimiser :
 Norme du tir (Force de la Frappe)
 
  - Fonction :
 Norme = f(d_g, angle) = k1*d_g + k2*angle
 
Get_init -> redefinir
Faire varier aleatoirement les variables dans les limites de nos Cond_init,
A chaque end_round ou max_steps ->
Mémoriser dans un tableau des couples k1,k2 les taux de réussites pour chaque valeur

 

 
  

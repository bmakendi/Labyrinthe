from upemtk import * #pour utiliser les trucs graphique
	
""" 
	Cette fonction va nous permettre de nous déplacer librement dans le fichier Labyrinthe
"""
	
def labyrinth(fichier):
	laby=[]
	ligne_laby=[]
	laby3=[]
	laby2=[]
	for ligne in fichier : 
		for n in ligne.split():
			ligne_laby.append(n)
		laby.append(ligne_laby)
	laby2=laby[1]
	for i in range(len(laby2)):
		laby3.append(list(laby2[i]))
	return laby3

"""
	On transforme les listes en chaîne de caractères, pour la réécrire dans un second fichier
"""

def labyrinth_chaine(laby,fichier):
	for e in laby:
		for s in e:
			fichier.write(s)
		fichier.write('\n')

	
"""
La fonction nouveau_laby réécrit le fichier texte Labyrinth dans un second fichier texte labyrinthe2. C'est dans ce fichier que se feront les modifications de Labyrinth grâce auxquels on pourra se déplacer.
"""

def nouveau_laby():
	fichier1=open('labyrinthe2.txt', 'w')
	fichier2=open('Labyrinth.txt', 'r')
	lecture=fichier2.readlines()
	for ligne in lecture:
		fichier1.writelines(ligne)
	fichier1.close()
	fichier2.close()

""" La fonction position_joueur nous permet de nous déplacer dans les listes que contient la liste laby, pour connaitre la position du joueur  @.

"""
		
def position_joueur(laby):
	position_j=[]
	for i in range(len(laby)):
		for j in range(len(laby[i])):
			if laby[i][j]=='@':
				position_j.append(i)
				position_j.append(j)
				return position_j
	
	
"""
La fonction position_sortie nous permet de nous déplacer dans les listes que contient la liste laby, pour la position de la sortie X .
"""
	
def position_sortie(laby):
	position_s=[]
	for i in range(len(laby)):
		for j in range(len(laby[i])):
			if laby[i][j]=='X':
				position_s.append(i)
				position_s.append(j)
				return position_s
				
"""FONCTIONS DE DEPLACEMENT
la fonction avancer echange le joueur '@' avec un '.' pour le faire avancer, idem pour reculer.
"""

def autorisation_avancer(laby, i, j):
	if laby[i-1][j]=='.':
		return True

def avancer(laby):
	lst_position=position_joueur(laby)
	i=lst_position[0]
	j=lst_position[1]
	if autorisation_avancer(laby, i, j)==True:
		temp=laby[i][j]
		laby[i][j]=laby[i-1][j]
		laby[i-1][j]=temp

#Si le joueur gagne, le jeu s'arrête et on vous propose de recommencer ou de quitter
def gagner(laby):
	lst_positionj=position_joueur(laby)
	lst_positions=position_sortie(laby)
	i=lst_positionj[0]
	j=lst_positionj[1]
	a=lst_positions[0]
	b=lst_positions[1]
	if laby[i+1][j]==laby[a][b]:
		return True
	return False
	
	
	

def autorisation_reculer(laby, i, j):
	if laby[i+1][j]=='.':
		return True
	
def reculer(laby):
	lst_position=position_joueur(laby)
	i=lst_position[0]
	j=lst_position[1]
	if autorisation_reculer(laby, i, j)==True:
		temp=laby[i][j]
		laby[i][j]=laby[i+1][j]
		laby[i+1][j]=temp
	
	
"""
On raisonne comme avec une matrice en transposant la liste laby, ensuite on échange les valeurs laby[i][jmax] avec laby[i][jmin] grâce à une fontion nommé retourne.
jmax et jmin étant les plus grands et plus petits indices.
Pour tourner vers la gauche, on fait une rotation vers la droite, et inversement.

"""
	
def retourne(lst):
	debut=0
	fin=len(lst)-1
	while debut < fin:
		temp=lst[debut]
		lst[debut]=lst[fin]
		lst[fin]=temp
		debut+=1
		fin-=1

def rotation_droite(laby):  #pour que le joueur tourne a droite
	laby[:] = list(map(list, zip(*laby)))
	for i in range(len(laby)):
		retourne(laby[i])

def rotation_gauche(laby):  #pour que le joueur tourne a gauche
	i=0
	while i<=2:
		rotation_droite(laby)
		i=i+1
		
"""
FIN DES FONCTIONS DE DEPLACEMENT
"""		

"""
FONCTIONS GRAPHIQUES
"""

#Tableau de commande
def tableau_commande():
	ligne(0, 350, 600, 350, couleur='black', epaisseur=1, tag='') 
	rectangle(200, 380, 455, 480, couleur='black', remplissage='', epaisseur=1, tag='')
	ligne(200, 430, 455, 430, couleur='black', epaisseur=1, tag='')
	ligne(285, 380, 285, 480, couleur='black', epaisseur=1, tag='')
	ligne(370, 380, 370, 480, couleur='black', epaisseur=1, tag='')
	fleche(327.5, 385,327.5, 470, couleur='black', epaisseur=3, tag='')#fleche du bas
	ligne(327.5, 435, 327.5, 470, couleur='black', epaisseur=1, tag='')
	fleche(327.5, 400,327.5, 385, couleur='black', epaisseur=3, tag='') #fleche du haut
	ligne(327.5, 425, 327.5, 385, couleur='black', epaisseur=1, tag='')
	fleche(232,408,212,408, couleur='black', epaisseur=3, tag='')# fleche de gauche
	ligne(272, 408, 212, 408, couleur='black', epaisseur=1, tag='')
	fleche(412,408,432,408, couleur='black', epaisseur=3, tag='') #fleche de droite
	ligne(385, 408, 432, 408, couleur='black', epaisseur=1, tag='')
	cercle(242.5,455, 15, couleur='black', remplissage='', epaisseur=1, tag='')#fleche de rotation gauche
	fleche(256.5,440,242,440, couleur='black', epaisseur=3, tag='')
	cercle(412.5, 455, 15, couleur='black', remplissage='', epaisseur=1, tag='')#fleche de rotation droite
	fleche(412,440,416.5,440, couleur='black', epaisseur=3, tag='')
	
#Cadre
def cadre():
	rectangle(1,1 , 599, 349, couleur='black', remplissage='', epaisseur=3, tag='')
	
#Les murs
def mur_cotedroit_dujoueur():
	ligne(550, 35, 550, 325, couleur='black', epaisseur=3, tag='')
	ligne(550, 35, 599, 0, couleur='black', epaisseur=3, tag='')
	ligne(550, 325, 599, 349, couleur='black', epaisseur=3, tag='')

def mur_cotegauche_dujoueur():
	ligne(50, 50, 50, 300, couleur='black', epaisseur=3, tag='')
	ligne(1, 1, 50, 50, couleur='black', epaisseur=3, tag='')
	ligne(0, 349, 50, 300, couleur='black', epaisseur=3, tag='')

def mur_devant_droite():
	ligne(400, 150, 400, 250, couleur='black', epaisseur=2, tag='')
	ligne(400,150,599,0,couleur='black', epaisseur=2, tag='')
	ligne(400,250,599,349, couleur='black', epaisseur=2, tag='')
	
def mur_devant_gauche():
	ligne(50, 50, 50, 300, couleur='black', epaisseur=2, tag='')
	ligne(50, 50, 150, 150, couleur='black', epaisseur=2, tag='')
	ligne(50, 300, 150, 250, couleur='black', epaisseur=2, tag='')
	ligne(150, 150, 150, 250 ,couleur='black', epaisseur=2, tag='')

def mur_loin_droit():
	rectangle(400, 150, 550, 250, couleur='black', remplissage='', epaisseur=1, tag='')

def mur_loin_milieu():
	rectangle(150, 150, 400, 250, couleur='black', remplissage='', epaisseur=1, tag='')
	
def mur_loin_gauche():
	rectangle(50, 150, 150, 250, couleur='black', remplissage='', epaisseur=1, tag='')
		
#Ecran d'accueil
def ecran_titre():
	texte(200, 100, 'LABYRINTHE', couleur='black', ancrage=NW, police="Purisa", taille=24, tag='')
	texte(250, 270, 'JOUER',couleur='black', ancrage=NW, police="Purisa", taille=24, tag='')
	texte(245, 350, 'QUITTER',couleur='black', ancrage=NW, police="Purisa", taille=24, tag='')

#Panneau d'avertissement: le joueur se trouve en face d'un mur et doit tourner à gauche ou à droite
def avertissement():
	texte(75, 100, 'Tournez à gauche ou à droite', couleur='black', ancrage=NW, police="Purisa", taille=24, tag='')
	
#Ecran de victoire
def ecran_victoire():
	texte(150, 100, 'VOUS AVEZ GAGNE', couleur='black', ancrage=NW, police="Purisa", taille=24, tag='')
	texte(175, 270, 'RECOMMENCER',couleur='black', ancrage=NW, police="Purisa", taille=24, tag='')
	texte(245, 350, 'QUITTER',couleur='black', ancrage=NW, police="Purisa", taille=24, tag='QUITTER')
		
"""
FIN DES FONCTIONS GRAPHIQUES
"""

	
def main():
	cree_fenetre(600,500)
	ecran_titre()
	mise_a_jour()
	fichier=open('Labyrinth.txt', 'r')
	fichier2=open('labyrinthe2.txt', 'w') 
	fichier3=open('labyrinthe2.txt', 'r') 
	nouveau_laby()
	laby=labyrinth(fichier)
	print(laby)
	lst_position=position_joueur(laby)
	i=lst_position[0]
	j=lst_position[1]
	print(position_sortie(laby))
	clic = attente_clic()
	x = clic[0]
	y= clic[1]
	if ((x>200 and x<400) and (y>350 and y<400)):
		ferme_fenetre()
	elif ((x>200 and x<380) and (y>270 and y<320)):
		efface_tout()
		while position_joueur(laby)!=[0, 18]:
			efface_tout()
			tableau_commande()
			lst_position=position_joueur(laby)
			i=lst_position[0]
			j=lst_position[1]
			mur_cotedroit_dujoueur()
			mur_cotegauche_dujoueur()			
			if laby[i-2][j]=='*':
				mur_loin_milieu()			
			if laby[i-2][j-1]=='*' and laby[i-1][j-1]!='*':
				mur_loin_gauche()			
			if laby[i-2][j+1]=='*' and laby[i-1][j+1]!='*':
				mur_loin_droit()			
			if laby[i-1][j]=='*':
				efface_tout()
				tableau_commande()
				avertissement()			
			if laby[i-1][j+1]=='*':
				mur_devant_droite()			
			if laby[i-1][j-1]=='*':
				mur_devant_gauche()			
			clic = attente_clic()
			x=clic[0]
			y=clic[1]
			if ((x>200 and x<285) and (y>380 and y<480)): #case rotation et tourner a gauche
				rotation_droite(laby)
				labyrinth_chaine(laby, fichier2)				
			if ((x>285 and x<370) and (y>380 and y<430)):
				avancer(laby)
				labyrinth_chaine(laby, fichier2)				
			if ((x>285 and x<370) and (y>430 and y<480)):
				reculer(laby)
				labyrinth_chaine(laby, fichier2)				
			if ((x>370 and x<455) and (y>380 and y<480)):
				rotation_gauche(laby)
				labyrinth_chaine(laby, fichier2)
			mise_a_jour()
		ecran_victoire()
	fichier.close()
	fichier2.close()
	fichier3.close()
	attente_clic()
	ferme_fenetre() 
	    
main()
			

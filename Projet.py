#projet semaine 1 partie 1 Thomas Petit

import os
import requests as rq
from bs4 import BeautifulSoup
import json

def ex1():
	r = rq.get(' https://api.github.com/repositories')
	results =r.json()
	fichier = open('listeajout.txt',"w")
	for ajout in results:		
		fichier.write(ajout['name'])
		if ajout['description']:
			fichier.write(' : '+ajout['description']+'\n')
		else:	
			fichier.write(' \n ')
	fichier.close()
	print("ex1")
	print("done")	
	
def ex2():

	r = rq.get('https://api.github.com/search/repositories?q=sort=stars&order=desc&pushed:>=2020-01-01')
	rep =r.json()
	repertory=rep['items']
	fichier = open('listerep.txt',"w")
	for R in repertory:
		fichier.write(R['name'] )
		if R['description']:
			fichier.write(' : '+R['description'])
		fichier.write(' notes : '+str(R['stargazers_count'])+'\n')
	fichier.close()
	print("ex1")
	print("done")

#ex3 : * * * * * /home/lithomas/Documents/BootCamp/J3/projet.py > /home/lithomas/Documents/BootCamp/J3/log.log


def ex4():
	AjoutGHurl = 'https://api.github.com/repositories'
	A = rq.get(AjoutGHurl)
	AjoutGH=A.json()	
	dico={}
	for ajout in AjoutGH:
		if ajout['description']:
			dico[ajout['name']]=ajout['description']
		else:
			dico[ajout['name']]="None"			
			
	repGHURL='https://api.github.com/search/repositories?q=sort=stars&order=desc&pushed:>=2020-01-01'
	R= rq.get(repGHURL)
	RepGH=R.json()
	for rep in RepGH['items']:
		if rep['description']:
			dico[rep['name']]=rep['description']+' ('+str(rep['stargazers_count'])+' stars)'
		else:
			dico[rep['name']]="None"+str(rep['stargazers_count'])+' stars'
	print(dico)
	datajson = json.dumps(dico,indent = 6)
	fichier = open('dicodata.json','a')
	fichier.write(datajson)
	fichier.close()
	print("ex4")
#pas aboutit.... lOGIQUE :
# On récupère les données avec le scrapping, on regarde si on a déjà des données de l'utilisateur afin de savoir les actions suiivante :
# 	le fichier n'existe pas : on en créé un avec la date d'aujourd'hui et le nom de l'utilisateur concerné 
# 	le fichier existe alors on récupère les données des différents noms de repertoire et les étoiles puis on écrase les anciennes données par les nouvelles et on compare les anciennes et les nouvelles pour savoir les différences d'étoiles et les nouveaux repertoires, on crée une alerte afin d'envoi en précisant les nouveaux repertoires et 'augmentation des étoiles
# 	pour l'automatiser on fait une commande cron qui repete le code tous les matins à 10H par exemple'
def ex5(Utilisateur):
	url='https://api.github.com/users/'+Utilisateur+'/repos'
	U=rq.get(url)
	RepUlt=U.json()
	fichier = open('data' +Utilisateur+now()+'.json','w')
	fichier.write(RepUlt)
	fichier.close()

	
ex5('ghivert')
print('done')
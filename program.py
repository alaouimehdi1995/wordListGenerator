'''
[a,a,a]
[1,1,1]
[a,a,b]

aaa
aab
aac
si on est dans le dernier caractère, on ajoute jusqu'à atteindre le max
sinon, on change le car par le suivant et on retourne au caractère suivant

...
zzz
zz0
zz1
...
999
aaaa
'''


Min=3
Max=4
chars=['a','b','c']
actualSize=Min
string=[]
index=[]
while(actualSize<=Max):
	string=[]
	index=[]
	for i in range(0,actualSize):
		string.append(chars[0])
		index.append(0)
	#string=['a','a','a'], index=[0,0,0]
	print(''.join(string))
	currentChar=actualSize-1
	currentIndex=0

	#initialisé
	while(currentChar>=0):
		
		if(index[currentChar]<len(chars)-1):
			index[currentChar]+=1
			string[currentChar]=chars[index[currentChar]]
			print(''.join(string))
			currentChar=len(string)-1
		else:
			index[currentChar]=0
			string[currentChar]=chars[index[currentChar]]
			currentChar-=1
	actualSize+=1
				
		

'''
Algorithme:
taille du mot=min
tant que la taille <max:
	on initialise un tableau string de la taille actuelle, entierement fait par chars[0]
	aussi un tableau index de la taille actuelle, entierement fait de 0
	le caractère courant est le dernier,
	tant qu'on n'a pas atteint le premier ( la fin)
	si on n'a pas encore fini chars pour le caractère actuel, on incrémente l'index du caractère actuel, on change le caractère, et on retourne à la fin de la chaine
	si on atteint la limite, on remet l'index actuel à 0, on change le caractère et le caractère courant devient celui qui le précède
'''
			


import sys
import re
files={'input':None,'output':None}
types={'lower':False,'upper':False,'number':False}

Min=3
Max=4
chars=['a','b','c','d','e']
'''
Args:
-a:minuscule
-A:majuscule
-n:nombre
-o,--output
-i, --input

'''
#def write():#doit écrire tout les 1000 mots
def getArgs():
	args=sys.argv[1:]
	if(len(args)>0):
		if "-o" in args or "--output" in args:
			files['output']=args[args.index('-o')+1] if '-o' in args else args[args.index('--output')+1]
		if "-i" in args or "--input" in args:
			files['input']=args[args.index('-i')+1] if '-i' in args else args[args.index('--input')+1]
		result = re.findall('-(a|A|n)(a|A|n)?(a|A|n)?', " ".join(args), re.DOTALL)
		result= [list(e) for e in result]
		resultArray=[]
		for e in result:
			resultArray+=e
		
		
		types['lower']=('a' in resultArray)
		types['upper']=('A' in resultArray)
		types['number']=('n' in resultArray)
		print(files)
		print(types)
		





getArgs()
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
	#print(''.join(string))
	currentChar=actualSize-1
	currentIndex=0

	#initialisé
	while(currentChar>=0):
		
		if(index[currentChar]<len(chars)-1):
			index[currentChar]+=1
			string[currentChar]=chars[index[currentChar]]
			#print(''.join(string))
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
			


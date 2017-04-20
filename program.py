import sys
import re


files={'input':None,'output':None}
types={'lower':False,'upper':False,'number':False}
limits={'min':3,'max':4}
authorizedChars=[]
wordBuffer=[] #Writing and emptying it when it's length=1000

#should add -c continue option (read wordlist and finish it)
#should decrease printing rate for files['output']!=None (optimizing)
def extractArgs():
	args=sys.argv[1:]
	if(len(args)>0): #if there is arguments
		#Extracting input,output,min and max arguments
		if "-o" in args or "--output" in args:
			files['output']=args[args.index('-o')+1] if '-o' in args else args[args.index('--output')+1]
		if "-i" in args or "--input" in args:
			files['input']=args[args.index('-i')+1] if '-i' in args else args[args.index('--input')+1]
		if "-m" in args or "--min" in args:
			limits['min']=int(args[args.index('-m')+1]) if '-m' in args else int(args[args.index('--min')+1])
		if "-M" in args or "--max" in args:
			limits['max']=int(args[args.index('-M')+1]) if '-M' in args else int(args[args.index('--max')+1])
		
		#extracting -a,-A,-n and their combinations using regex
		result = re.findall('-(a|A|n)(a|A|n)?(a|A|n)?', " ".join(args), re.DOTALL)
		result = [list(e) for e in result]
		resultArray=[]
		for e in result:
			resultArray+=e
		
		types['lower']=('a' in resultArray)
		types['upper']=('A' in resultArray)
		types['number']=('n' in resultArray)
		limits['max']=limits['min'] if limits['max']<limits['min'] else limits['max']	#in case min > max
		
		#Creating the authorized characters final list

		global authorizedChars
		if(files['input']):
			try:
				authorizedChars=''.join(open(files['input'],'r').readlines())
			except:
				print("Input file not found or not authorized, exiting..")
				exit(0)
			authorizedChars=list(authorizedChars)
			authorizedChars=[e for e in authorizedChars if (e!=" " and e!="")]

		else:
			if(types['lower']):
				for e in range(97,123): #97 is 'a' 's ASCII, 122 is for 'z'
					authorizedChars.append(chr(e))
			if(types['upper']):
				for e in range(65,91):
					authorizedChars.append(chr(e))
			if(types['number']):
				for e in range(48,58):
					authorizedChars.append(chr(e))
		authorizedChars=sorted(set(authorizedChars))
		
	else:
		print("There is no arguments, exiting..")
		exit(0)
		
def dumpBuffer(string,lastIteration=False):
	global wordBuffer
	print(string)
	if(files['output']):
		wordBuffer.append(string)
		
		if(len(wordBuffer)==1000 or lastIteration==True):
			
			file=open(files['output'],"a")
			for e in wordBuffer: file.write(e+"\n")
			file.close()
			wordBuffer=[]







extractArgs()

actualSize=limits['min']
string=[]
index=[]

while(actualSize<=limits['max']):
	string=actualSize*[authorizedChars[0]]
	index=actualSize*[0]
	#string=['a','a','a'], index=[0,0,0]
	dumpBuffer(''.join(string))
	currentChar=actualSize-1
	currentIndex=0

	while(currentChar>=0):
		
		if(index[currentChar]<len(authorizedChars)-1):
			index[currentChar]+=1
			string[currentChar]=authorizedChars[index[currentChar]]
			dumpBuffer(''.join(string))
			currentChar=len(string)-1
		else:
			index[currentChar]=0
			string[currentChar]=authorizedChars[index[currentChar]]
			currentChar-=1
	dumpBuffer(''.join(string),True)
	actualSize+=1
				
		

'''
Algorithme:
taille du mot=min
tant que la taille <max:
	on initialise un tableau string de la taille actuelle, entierement fait par authorizedChars[0]
	aussi un tableau index de la taille actuelle, entierement fait de 0
	le caractère courant est le dernier,
	tant qu'on n'a pas atteint le premier ( la fin)
	si on n'a pas encore fini authorizedChars pour le caractère actuel, on incrémente l'index du caractère actuel, on change le caractère, et on retourne à la fin de la chaine
	si on atteint la limite, on remet l'index actuel à 0, on change le caractère et le caractère courant devient celui qui le précède
'''
			


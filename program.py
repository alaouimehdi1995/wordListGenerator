'''
WordList Generator Algorithm, conceived and implemented by: ALAOUI Mehdi 2017
'''
import sys
import re


files={'input':None,'output':None}
types={'lower':False,'upper':False,'number':False}
limits={'min':3,'max':4}
authorizedChars=[]
wordBuffer=[] #Writing and emptying it when it's length=1000

'''
To do:
	-Adding -h help section
	-Adding -c argument to continue the wordlist from existing one
	-Adding bruteforce option (zip, rar, etc)
	-Adding -r regex wordlist if possible
'''

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
			if(len(authorizedChars)==0):
				print("Specified file doesn't contain valid characters, exiting..")
				exit(0)

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


def dumpBuffer(word=""):
	global wordBuffer

	if(files['output']):
		wordBuffer.append(word)
		
		if(len(wordBuffer)==1000 or not word):
			print(word)						#printing one word in 1000 iterations is 4x faster than printing all words
			file=open(files['output'],"a")
			for e in wordBuffer: file.write(e+"\n")
			file.close()
			wordBuffer=[]
	else:
		print(word)


#Main program

extractArgs()

wordSize=limits['min']
word=[]
index=[]

while(wordSize<=limits['max']):
	word=wordSize*[authorizedChars[0]]
	index=wordSize*[0]
	#word=['a','a','a'], index=[0,0,0]
	dumpBuffer(''.join(word))
	currentChar=wordSize-1
	currentIndex=0

	while(currentChar>=0):
		
		if(index[currentChar]<len(authorizedChars)-1):
			index[currentChar]+=1
			word[currentChar]=authorizedChars[index[currentChar]]
			dumpBuffer(''.join(word))
			currentChar=len(word)-1
		else:
			index[currentChar]=0
			word[currentChar]=authorizedChars[index[currentChar]]
			currentChar-=1
	wordSize+=1

dumpBuffer()

			


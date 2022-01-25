

import new_sentiment_mod as s
import pickle 
import pandas as pd
import re
import collections
import nltk
from Cleaning1 import ProcessTweet
from Cleaning1 import Segmentation
from textblob import TextBlob
import matplotlib.pyplot as plt
from SWN import sentiwrd

df1=pd.read_csv("testing_data_copy.txt",error_bad_lines=False, sep=" ", header=None)
sentences = df1[1]

def ML_approach(txt, pol):

	ml = ''
	print (s.sentiment(txt))
	label,conf = s.sentiment(txt)
	return label

def subject(txt):
	flag = 0
	tokens = txt.split()
	tokenpos = nltk.pos_tag(tokens)
	for words,pos in tokenpos:
		if pos.startswith("PR"):
			flag = 1
		if pos.startswith("NNP"):
			flag = 1
	return flag

def transform():

	i = 0
	ProcT = collections.defaultdict(dict)
	true_polarity = df1[0]
	xml = []
	yn = []
	z = []
	axis = []

	for index in range(0,len(df1)):
		
		print index
		txt = df1[1][index]
		pol = df1[0][index]
		flag = subject(txt)

		if (flag == 1):
			#Removing URLs
			txt = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', txt)
			
			emoji, emj_pol = Segmentation(txt)
			newTweet = ' '.join(ProcessTweet(txt.split()))
			
			ProcT[i]['Tweet'] = newTweet
			ML_label = ML_approach(newTweet, pol)

			if ML_label == 'neg' :
				wn, n = sentiwrd(newTweet)
			ProcT[i]['ML'] = label	xml.append((label/5)
			
			ProcT[i]['Without Nouns'] = wn
			ProcT[i]['Nouns'] = n
			yn.append(n)
			ProcT[i]['Emojis'] = emoji
			z.append(level)
			axis.append(index)
			i = i+1

	for a in ProcT:
		print("\n")
		print a
		print ProcT[a]

	with open('TestEnt.pickle', 'wb') as handle:
   		pickle.dump(ProcT, handle, protocol=pickle.HIGHEST_PROTOCOL)
 
 	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.plot( axis,xml, label = "ML", alpha = 0.7)
	ax.plot( axis,yn, label = "SWN", alpha = 0.7)
	ax.autoscale()
	plt.xlabel('x - axis')
	plt.ylabel('y - axis')
 	plt.legend(loc='upper left')
	plt.title('Comparing Sentiments of ML and Knowledge Based Approach')
	plt.show()

 
transform()
print("Done")




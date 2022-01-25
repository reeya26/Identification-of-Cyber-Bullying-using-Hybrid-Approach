

# -*- coding: utf-8 -*-
import pandas as pd
import nltk
import string
import re
import csv
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from autocorrect import spell			
#nltk.download('wordnet') 

txt = ("NOPE!  😭😭 It was horrible graat #Kim Jones last show and wanted to snap a dying LV pic ðŸ˜‚  :D How http://mysonikudi.com")
token = txt.split()

emj = []
emjB = []
emj_pol = []
emj_desc = []

def Segmentation(txt):

	emoji=pd.read_csv("Final Emoji1.csv")
	le = len(emoji)

	for i in range(0,le):
		e = emoji.iloc[i,1]
		if str(e) in txt :
			txt = re.sub(r'e'," "+e+" ", txt)

	tokens = txt.split()
	lt = len(tokens)

	for t in range(0,lt):
		for i in range(0,le):
			if tokens[t] == emoji.iloc[i,1]:
				print (tokens[t])
				emj.append(emoji.iloc[i,1])
				emj_pol.append(emoji.iloc[i,3])
				emj_desc.append(emoji.iloc[i,4])	
				break

	if len(emj) == 0:
		avgp = 0
	else :	
		avgp = sum(emj_pol)/len(emj_pol)
	return emj, avgp


def ProcessTweet(token):

	tokens = [w.lower() for w in token]

	reader = csv.reader(open('slang_dict2.csv', 'r'))
	d = {}
	for row in reader:
   		k, v = row
   		d[k] = v
	divs = tokens
	new_divs = []

	for index, div in enumerate(divs):
		if div in d:
			new_divs.append(d[divs[index]])
		else:
			new_divs.append(divs[index])

	tokens = new_divs

	## This is done so that slangs like LOL containing multiple words are tokenized
	tok_str = ' '.join(tokens)
	tokens = tok_str.split()
	tokens = [word for word in tokens if word.isalpha()]

	newT = []
	for token in tokens:
		newT.append(spell(token))

	wnl = WordNetLemmatizer()
	lemm = [wnl.lemmatize(word,'v') for word in newT]
	
	return lemm

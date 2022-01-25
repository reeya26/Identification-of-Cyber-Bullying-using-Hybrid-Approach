

# -*- coding: utf-8 -*-
import pandas as pd
import nltk
import string
import re
import csv
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from autocorrect import spell	
from nltk.corpus import sentiwordnet as swn		
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk
import sys

test1 = ("I hate her she's fucking annoying and horrible")


def sentiwrd(test1, flag = 1):
	
	
	tokens = test1.split()
	print(tokens)

	#print("\nPOS Tagging :")
	tokenpos = nltk.pos_tag(tokens)
	#print (tokenpos)

	if flag is 1:
		new_words = []
		for word,pos in tokenpos:

			if pos.startswith("NN"):
				pos = "n"
			elif pos.startswith("R"):
				pos = "r"
			elif pos.startswith("V"):
				pos = 'v'
			elif pos.startswith("JJ"):
		 		pos = 'a'
			new_words.append([word,pos])

		#print("\nFiltering out Stop Words : ")
		stop_words = set(stopwords.words('english'))
		words=[]
		for word,pos in new_words:
			if word in stop_words:
				continue
			words.append([word,pos])


		new_w=[]
		for w,p in words:
			ambiguous = w
			new_w.append(w)


		withoutnouns=[]
		for w,p in words:
			if p == 'n' :
				continue
			elif p == 'PRP' :
				continue
			withoutnouns.append(w)


		open("outputfile.txt","w+")
		for i in new_w:

			filename  = open("outputfile.txt","a")
			sys.stdout = filename
			print(lesk(new_w,i))

		open("withoutnouns.txt","w+")
		for i in withoutnouns:
			filename = open("withoutnouns.txt","a")
			sys.stdout = filename
			print(lesk(withoutnouns,i))

		sys.stdout = sys.__stdout__

		temp='None'
		sumpos=0
		sumneg=0
		totalscore_n = 0
		f=open("outputfile.txt","r")
		f1 = f.readlines()
		count=0
		for i in f1:
			
			if i.startswith("None"):
				continue
			y = (i[i.find("(")+1:i.find(")")])

			extracted_text = re.search('''(?<=')\s*[^']+?\s*(?=')''', y)

			z=swn.senti_synset(extracted_text.group().strip())
			sumpos = sumpos+z.pos_score()
			sumneg=sumneg+z.neg_score()
			count=count+1
			


		# print("METHOD ONE - WITH NOUNS")
		if count == 0 :
			avgpos = 0
			avgneg = 0
		else :	
			avgpos=sumpos/count
			avgneg=sumneg/count
		totalscore_n = avgpos-avgneg

		fnew=open("withoutnouns.txt","r")
		f2 = fnew.readlines()
		count=0
		sumpos=0
		sumneg=0
		totalscore_wn=0
		for i in f2:
			if i.startswith("None"):
				continue
			y = (i[i.find("(")+1:i.find(")")])

			extracted_text = re.search('''(?<=')\s*[^']+?\s*(?=')''', y)
			z=swn.senti_synset(extracted_text.group().strip())
			sumpos = sumpos+z.pos_score()
			sumneg=sumneg+z.neg_score()
			count=count+1

		#print("METHOD TWO - WITHOUT NOUNS")
		if count == 0 :
			avgpos = 0
			avgneg = 0
		else :	
			avgpos=sumpos/count
			avgneg=sumneg/count


		final_method2=[avgpos,avgneg]
		totalscore_wn = avgpos-avgneg


	return totalscore_wn,totalscore_n

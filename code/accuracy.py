

import pickle
import matplotlib.pyplot as plt
from collections import Counter

true_pos = 0 
false_pos = 0
true_neg = 0
false_neg = 0	

def accuracy(ml, swn):

	val = ""

	if ml > 0 and swn > 0:
		val = "tp"

	elif ml > 0 and swn <= 0:
		val = "fp"

	elif ml <= 0 and swn <= 0:
		val = "tn"

	elif ml <= 0 and swn > 0:
		val="fn"	
	return val



def final_flagging(emoj_polarity, text_polarity):

	flag = ""

	if emoj_polarity >= 0 and text_polarity >= 0 :
		final_polarity = "pos"
		flag = "Positive"

	elif emoj_polarity <0 and text_polarity<0 :
		final_polarity = "neg"
		if text_polarity <0 and text_polarity > -0.25 : 
			flag = "Level 4 Negative"
		elif text_polarity < -0.25 and text_polarity > -0.5 :
			flag = "Level 3 Negative"
		elif text_polarity < -0.5 and text_polarity > -0.75 :
			flag = "Level 2 Negative"
		elif text_polarity < -0.75 and text_polarity >= -1 :
			flag = "Level 1 Negative"

	elif (emoj_polarity >0 and text_polarity<0) or (emoj_polarity <0 and text_polarity>0) :
		final_polarity = "irony"
		flag = "Irony"	
	return flag


def calc():


	true_pos = 0 
	false_pos = 0
	true_neg = 0
	false_neg = 0	
	fl0 = fl1 = fl2= fl3 = fl4 = fli= 0

	with open(r"10000Ent.pickle", "rb") as input_file:
		ProcT = pickle.load(input_file)

	for i in range(0,len(ProcT)):
		ml  = ProcT[i]['ML']
		swn = ProcT[i]['Nouns']
		emj = ProcT[i]['Emojis']
		polAgg = accuracy(ml,swn)
		pol = (ml+swn)/2
		flag = final_flagging(emj,pol)
		ProcT[i]['Level'] = flag

		if polAgg == "tp":
			true_pos = true_pos+1
		elif polAgg == "fp":
			false_pos = false_pos+1
		elif polAgg == "tn":
			true_neg = true_neg+1
		else:
			false_neg = false_neg+1	


		if flag== "Positive":
			fl0 = fl0 + 1
		elif flag== "Level 4 Negative":
			fl4 = fl4 + 1	
		elif flag== "Level 3 Negative" :
			fl3 = fl3 + 1
		elif flag== "Level 2 Negative" :
			fl2 = fl2 + 1
		elif flag== "Level 1 Negative" :
			fl1 = fl1 + 1
		else:
			fli = fli + 1

		print ("\nML + SWN = " + str(polAgg))		
		print ("EMJ + SWN = " + str(flag))


	activitiesPol = ['True Positive', 'False Positive', 'True Negative', 'False Negative']
	activitiesLvl = ['Positive', 'Level 4 Neg', 'Level 3 Neg','Level 2 Neg','Level 1 Neg']

	slicesPol = [true_pos, false_pos, true_neg, false_neg]
 	slicesLvl = [fl0,fl4,fl3,fl2,fl1]

	colorsPol = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
	colorsLvl = ['#01d0ee','#ecee01','#ecad17','#ea5809','#ea2b09']


	plt.pie(slicesLvl, colors=colorsLvl, 
        startangle=90, shadow = True, explode = (0.1, 0.1, 0.1, 0.3,0.5),
        radius = 1.2, autopct = '%1.1f%%')
	plt.legend(activitiesLvl)
	plt.show()	

	plt.pie(slicesPol, labels = activitiesPol, colors=colorsPol, 
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')
	plt.show()

calc()


	

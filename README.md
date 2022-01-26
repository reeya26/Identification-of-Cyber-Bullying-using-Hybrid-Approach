# Identification of Cyber Bullying using Hybrid Approach in Sentiment Analysis

This project was part of my Undergraduate Thesis. This was a cause that was important to all of us, due to the rising number of death threats and rape threats received by people voicing their opinion on social media. There are also a large number of youngsters present online, who might be more prone to depression and anxiety. As free speech is also a democratic right, we tried to segregate the tweets that are extremely negative and are targeted at a specific person, and which can be flagged down for removal.

The research paper was presented and published with [IEEE Xplore](https://ieeexplore.ieee.org/document/9001476)

## Description of all functions

* **data_collection.py** uses the Tweepy API to extract tweets as per the filter entered by the user (eg. timeline, geography, etc)
* **data_preprocessing.py** works on cleaning and segmenting the data into text and emoticons
* **knowledge_algo.py** uses a lexicon for opinion mining called, SentiWordNet, to assign polarity to each tweet. A separate database assigns polarity to the emoticons.
* **ml_algo.py** uses a Bagging Classifier including Naive Bayes and Linear Support Vector Machine to assign a polarity of either 0 or 1 to a tweet,thereby reaffirming the value given by SentiWorkNet. The trained dataset is stored as a pickle file.
* **main.py** calls all the functions to iterate over a series of tweets.
* **accuracy.py** uses a Confusion Matrix to calculate the accuracy of the algorithm "With Nouns". The classification algorithm is 70.3% accurate.



## Architecture Diagram

Our framework consists of three main steps, which includes knowledge based sentiment analysis, whose result is then reinforced with machine learning based analysis. The resulting polarity is then aggregated with the polarity obtained from the emoticons, which segregates the tweets into varying levels of positive and negative text.

<img width="288" alt="Screen Shot 2022-01-25 at 1 22 06 PM" src="https://user-images.githubusercontent.com/22598639/151062134-e685da95-c195-4e5b-8456-9c61343b4e3a.png">


**Comparing Sentiments of Knowledge-Based Approach and Machine Learning Approach.**
<img width="604" alt="Screen Shot 2022-01-25 at 1 14 09 PM" src="https://user-images.githubusercontent.com/22598639/151060854-be6aa6e5-00fa-4b9d-912f-0ceb105aa53d.png">


**The Resulting Confusion Matrix**

<img width="458" alt="Screen Shot 2022-01-25 at 1 15 57 PM" src="https://user-images.githubusercontent.com/22598639/151061079-20e49ebf-7903-4bfd-ba1b-4299a878756d.png">



## Final Classfication

Using the Knowledge-Based approach allowed us to obtain the "Degree of Negativity" of tweets. Cyber Bullying Tweets were more negative than the rest, and were labelled "Level 1 Neg" tweets, where the Negative Tweets ranged from Level 1 to Level 4. 
The resulting classfication is presented below, which states that **0.1% of tweets are Cyber Bullying Tweets**.

<img width="456" alt="Screen Shot 2022-01-25 at 1 16 26 PM" src="https://user-images.githubusercontent.com/22598639/151062001-5f28cc61-224d-48d3-b99c-c8fee42d3bc0.png">

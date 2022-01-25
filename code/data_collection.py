

import tweepy
import pandas as pd
import pickle
import csv
import nltk
import collections

consumer_key = 'tOfGFCaFpSuQoFK7KvhWzCQsN'
consumer_secret = 'cu8j8o7sYX6NyT1K2sAdnpzTDHsJi5KM7UTJwTx8w8y6t0SWR5'
access_token = '4581274574-Z1EMcdcOR2ESlcFCWHbZdXGy58eAfCAdgQXvTpl'
access_token_secret = 'HCykZlOy00opRdmJfLswKbvFfhSdblaLDU9IoXHUsLa4v'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
results = []

#Get the first 5000 items based on the search query
for tweet in tweepy.Cursor(api.search, q='love',lang="en").items(10):
    results.append(tweet)

##### IMPORTANT FUNCTIONS ####
def toDataFrame(tweets):

    DataSet = pd.DataFrame()

    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    return DataSet

#Pass the tweets list to the above function to create a DataFrame
DataSet = toDataFrame(results)
print(DataSet.tweetText)

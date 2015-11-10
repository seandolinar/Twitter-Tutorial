__author__ = 'seandolinar'

import json
import csv

'''
creates a .csv file using a Twitter .json file
the fields have to be set manually
'''

data_json = open('raw_tweets.json', mode='r').read() #reads in the JSON file into Python as a string
data_python = json.loads(data_json) #turns the string into a json Python object

csv_out = open('tweets_out_ASCII.csv', mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = ['created_at', 'text', 'screen_name', 'followers', 'friends', 'rt', 'fav'] #field names
writer.writerow(fields) #writes field

for line in data_python:

    #writes a row and gets the fields from the json object
    #screen_name and followers/friends are found on the second level hence two get methods
    writer.writerow([line.get('created_at'),
                     line.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
                     line.get('user').get('screen_name'),
                     line.get('user').get('followers_count'),
                     line.get('user').get('friends_count'),
                     line.get('retweet_count'),
                     line.get('favorite_count')])

csv_out.close()




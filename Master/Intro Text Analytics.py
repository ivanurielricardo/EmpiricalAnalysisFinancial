import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer

url = 'https://raw.githubusercontent.com/amjassem/DxU-Intro-to-Text-Analytics/main/Data/trump_tweets.csv'

# After some work reinstalling the certificates on my python, I was able to finally download the dataset and have python
# read the data needed. This is all assuming we then have data to work with.

# Read columns 1, 5, 6 and 7. Parse the dates
tweetData = pd.read_csv(url, usecols=[1, 5, 6, 7], parse_dates=[3])

# Print top 20 rows
print(tweetData.head(20))

# Task 1 is then to clean the code a bit
# things to consider are to remove url links, remove account handles and emails, remove strings that contain numbers,
# remove hashtags



def CleanText(text):

  # Removes URLs
  text = re.sub('(http|ftp|https)[^\s]*', '', text)
  # Removes account handles
  text = re.sub('@[^\s]*', '', text)
  # Removes emails
  text = re.sub('[^\s]+@[^\s]\.\[^\s]+', '', text)
  # Remove strings with numbers (e.g. "401k")
  text = re.sub('[^\s]*[0-9]+[^\s]*', '', text)

  return text

# Test on a couple of tweets
sel = [40, 95, 976, 32140]

for i in sel:
  print("===================")
  print(tweetData.text[i])
  print(CleanText(tweetData.text[i]))

############### Vectorization ###############

# Get the text of the tweets
texts = [CleanText(text) for text in tweetData.text]

# The object for vectorizing the corpus
vecCounts = CountVectorizer(stop_words='english')
# Vectorize the corpus
counts = vecCounts.fit_transform(texts)




# Print the vocabulary
vocabulary = vecCounts.get_feature_names_out()
print('Number of terms:', len(vocabulary))
print(vocabulary[0:100])



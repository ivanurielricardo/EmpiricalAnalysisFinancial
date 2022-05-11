#### KEEP THE CONSUMER KEYS AND TOKENS SECRET

import tweepy

auth = tweepy.OAuthHandler('iMufVpS0LRTONee4MwOarl4eR', 'exGavbqONJGNjRkBq3u4TMRvTcDRCHp8rFbQNDz3ArwiZzBJ0T')
auth.set_access_token('1512326611848372230-rsU8c1Cfp8gqk98vyYkiTT0cyjtuxg', 'cLJQ8hQkWxEBCT4kFJ5YNRFp3JsoIsz6G56YZ9fXrT8Wk')
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

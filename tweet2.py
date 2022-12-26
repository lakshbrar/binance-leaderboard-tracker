import tweepy

client = tweepy.Client(
	consumer_key = "",
	consumer_secret= "",
	access_token= "",
	access_token_secret = ""
)

def tweet_now(tweet_story):

    response = client.create_tweet(text = tweet_story)

    return response 
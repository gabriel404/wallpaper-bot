import tweepy
import time
import imgurbot
users_id = []

class TwitterStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		getuserInfo(status)
		replyTweet(status)

	def on_error(self, status_code):
		if status_code == 403:
			print("Acesso Negado.")
			return False

def getuserInfo(tweet):
	if tweet.user.id not in users_id: # print user info if hes not on the array already
		users_id.append(tweet.user.id)	
		print("User ID \t:" + str(tweet.user.id))
		print("User Name \t:" + tweet.user.name)
		print("User Screen name \t:" + tweet.user.screen_name)

def replyTweet(tweet):
	usr = tweet.user.screen_name
	name = tweet.user.name
	tweetid = tweet.id
	linkID = imgurbot.returnID()
	api.update_status("@{0} Olá {1}, aqui está seu link: {2}".format(usr, name, linkID), # message to be displayed 
	 in_reply_to_status_id = tweetid) # tweetid to reply to

if __name__ == '__main__':

	# codes for the bot account
	CONSUMER_KEY = ""
	CONSUMER_SECRET = ""
	ACCESS_KEY = ""
	ACCESS_SECRET = ""

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.secure = True
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,
		retry_count=10, retry_delay=5, retry_errors=5)

	streamListener = TwitterStreamListener() # creates an instance of the class
	myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

	myStream.filter(track=['#rndIMGur1'], async=True) # search for any tweet with the hashtag

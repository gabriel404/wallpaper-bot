<h1>Disclaimer</h1>

Right now the bot can send any image from Imgur, since I need to make an album with Wallpapers for it to work properly due to limitations on imgur's API (or myself, I'm too lazy)

<h1> REQUIREMENTS </h1>

	pip install imgurpython
	pip install tweepy
	Python 3.5
	
<h1>CONFIGURATION</h1>
<b>tweetbot.py</b>

You will need to create a new twitter app on apps.twitter.com, and put the correspondent keys on each field.


	CONSUMER_KEY = ""
	CONSUMER_SECRET = ""
	ACCESS_KEY = ""
	ACCESS_SECRET = ""
	
<b>imgurbot.py</b>

Do the same thing, except this time you'll need keys from Imgur, and replace the following lines:

	client_id = ""
	client_secret = ""

If you want to change the hashtag need to activate the bot just change the last line on <b>tweetbot.py</b>

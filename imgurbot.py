from imgurpython import ImgurClient
import random

client_id = ""
client_secret = ""
client = ImgurClient(client_id, client_secret)

links = []

items = client.gallery()
for item in items:
    links.append(item.link)

def returnID():
	x = random.randrange(0, len(links))
	return links[x]

from imgurpython import ImgurClient
import random

client_id = "757bbfa74a1ec01"
client_secret = "312d6a7c390c03a562967348f8b25e52aeaa4603"
client = ImgurClient(client_id, client_secret)

links = []

items = client.gallery()
for item in items:
    links.append(item.link)

def returnID():
	x = random.randrange(0, len(links))
	return links[x]

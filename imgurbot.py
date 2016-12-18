from imgurpython import ImgurClient
import random

client_id = ""
client_secret = ""
client = ImgurClient(client_id, client_secret)

links = []

items = client.gallery(section="/r/wallpapers", sort="top", window="all") #gets image links from wallpaper section
for item in items:
    links.append(item.link) #put all links on an array

def returnID(): # get a random link from links array and returns it
	x = random.randrange(0, len(links))
	return links[x]

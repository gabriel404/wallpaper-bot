import tweepy, time, sys

#	argfile = str(sys.argv[1]) # argumento com caminho do arquivo de texto

# chaves para autenticação
CONSUMER_KEY = consumerkey
CONSUMER_SECRET = consumersecret
ACCESS_KEY = accesskey
ACCESS_SECRET = accesssecret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#final da autenticação

twt = api.search(q="#randomhashtag")

t = ['#randomhashtag']

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "{0}, TESTE CONCLUIDO!".format(sn)
            s = api.update_status(m, s.id)
'''

api.update_status(argfile)
print("Status atualizado com sucesso!")
quit()


filename = open(argfile,'r')
f = filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900) #Tweet every 15 minutes
'''

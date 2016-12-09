import tweepy, time, sys

#	argfile = str(sys.argv[1]) # argumento com caminho do arquivo de texto

# chaves para autenticação
CONSUMER_KEY = "qxmcDRG923lXzlw4tysnAz5F9"
CONSUMER_SECRET = "sezRCwGQXzsfhtVg94YjBOVC2256SYyasE4jEqAjKrrgy109Xf"
ACCESS_KEY = "775135705098031105-mCwgEe0loDigwTTGI1TeZ4CAgaQHAHC"
ACCESS_SECRET = "vlPDlnaTjCd2wlfnq8kSlVK8WbehbyulZNOCgeaj4ItZx"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#final da autenticação

twt = api.search(q="#testandomalditobot")

t = ['#testandomalditobot']

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
from instabot import Bot

bot = Bot()
bot.login(username = 'xxxxxxx',password = 'xxxxxx')

bot.api.search_location(u"Tehran")
finded_location = bot.api.last_json['items'][0]
print(finded_location)
print(u"Found {}".format(finded_location['title']))
print(finded_location['location']['lng'], finded_location['location']['lat'])






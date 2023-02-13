# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cassiopeia as cass

f = open("api_key.txt", "r")
api = f.read()
f.close()

cass.set_riot_api_key(api)  # This overrides the value set in your configuration/settings.

summoner = cass.get_summoner(name="CanYouLimbo", region="NA")
print("{name} is a summoner on the {region} server.".format(name=summoner.name,
                                                                          region=summoner.region))

for match in summoner.match_history:
    for player in match.participants:
        print(player.runes)
    if(summoner in match.participants):
        print("I'm there!")
        break
    
        
    





# champions = cass.get_champions(region="NA")
# random_champion = random.choice(champions)
# print("He enjoys playing champions such as {name}.".format(name=random_champion.name))

# challenger_league = cass.get_challenger_league(queue=cass.Queue.ranked_solo_fives)
# best_na = challenger_league[0].summoner
# print("He's not as good as {name} at League, but probably a better python programmer!".format(name=best_na.name))


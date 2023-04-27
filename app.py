
"""

This specific code segment is to calculate my winrate over a certain number of games 
where I played Summon Aery Akali. 
There is an infinite loop when I choose a number over how many games I've played

"""
# import cassiopeia as cass

# f = open("api_key.txt", "r")
# api = f.read()
# f.close()

# cass.set_riot_api_key(api)  # This overrides the value set in your configuration/settings.

# summoner = cass.get_summoner(name="CanYouLimbo", region="NA")

# wins = 0
# total_games = 0
# user_input = ""

# while(not user_input):
#     try:
#         user_input = int(input("Enter how many summon Aery akali games you want to use for winrate: "))
#     except ValueError:
#         print("thats not a number silly!")


# for match in summoner.match_history:
#     p = match.participants[summoner]
#     if(p.runes.keystone.name == "Summon Aery" and p.champion.name == "Akali"):
#         if(p.team.win):
#             wins += 1
#         total_games += 1
#         user_input -= 1
#         if(user_input < 1):
#             break

# winrate = (100 * (wins / total_games))
# print(f"Using summon aery on akali, you have a {winrate}% winrate, yayyyy")


"""

This segment of code was used to Ask the user what champ and what rune they
wanted to use to get the winrate
But, it has the same problem of using num_of_games...theres no way to know
how many games you've played using that setup!

"""

# import cassiopeia as cass

# f = open("api_key.txt", "r")
# api = f.read()
# f.close()

# cass.set_riot_api_key(api)  # This overrides the value set in your configuration/settings.

# summoner = cass.get_summoner(name="CanYouLimbo", region="NA")

# wins = 0
# total_games = 0
# num_of_games = 0

# champ = input("Enter a champion: ")
# rune = input("Enter a rune: ")
# while(not num_of_games):
#     try:
#         num_of_games = int(input("How many games should we take into account"))
#     except ValueError:
#         print("thats not a number silly!")


# history = summoner.match_history

# for match in history:
#     p = match.participants[summoner]
#     if(p.runes.keystone.name == rune and p.champion.name == champ):
#         if(p.team.win):
#             wins += 1
#         total_games += 1
#         num_of_games -= 1
#         if(num_of_games < 1):
#             break

# winrate = (100 * (wins / total_games))
# print(f"Using {rune} on {champ}, you have a {winrate}% winrate, yayyyy")


"""

This is HUGEEEE! Instead of guessing how many games I have, I make a new list
of the filtered games, and then just loop through it! this is niiiice. 
AND i got a new divide by zero error when I tryed to divide by zero games, when the
filtered list was empty, so i just catch the exception, and say that they dont
have any games in their last 30 games!
Next, I want to make it so they don't have to put a champ or a rune, and then
it will just take all the games into account!


"""
# import cassiopeia as cass

# f = open("api_key.txt", "r")
# api = f.read()
# f.close()

# cass.set_riot_api_key(api)  # This overrides the value set in your configuration/settings.

# summoner = cass.get_summoner(name="CanYouLimbo", region="NA")

# wins = 0
# total_games = 0


# champ = input("Enter a champion: ")
# rune = input("Enter a rune: ")
# game = 0
# game_limit = 30
# filtered_history = []


# history = summoner.match_history

# for match in history:
#     if(game == game_limit):
#         break
#     game +=1
#     p = match.participants[summoner]
#     if(p.runes.keystone.name == rune and p.champion.name == champ):
#         filtered_history.append(match)


# for match in filtered_history:
#     p = match.participants[summoner]
#     if(p.team.win):
#         wins += 1
#     total_games += 1
# try:
#     winrate = (100 * (wins / total_games))
# except ZeroDivisionError:
#     print(f"You dont have any games playing {champ} using {rune} in your last {game_limit} games")
# else:
#     print(f"Using {rune} on {champ}, you have a {winrate}% winrate, yayyyy")


"""

I have successfully made the user be able to filter by keystone, champion, or both. but now, I cannot 
filter by...nothing! it doesn't work when i hit enter twice, just wanting my overall winrate! Ill try to make a 
separate code segment JUST for the overall winrate, and see if that helps

"""


# import cassiopeia as cass

# f = open("api_key.txt", "r")
# api = f.read()
# f.close()

# cass.set_riot_api_key(api)  # This overrides the value set in your configuration/settings.

# summoner = cass.get_summoner(name="CanYouLimbo", region="NA")

# wins = 0
# total_games = 0
# game_limit = 200
# game = 0
# history = summoner.match_history
# champ = input("Enter a champion (Enter nothing to look at all champs): ")
# keystone = input("Enter a keystone (Enter nothing to look at all keystones): ")


# def filter_by_both(match_history, champion, keystone): #return filtered match history
#     filtered_history = []
#     game = 0
#     for match in match_history:
#         print(game)
#         if(game == game_limit):
#             break
#         game +=1
#         p = match.participants[summoner]
#         if(p.runes.keystone.name == keystone and p.champion.name == champ):
#             print("found one")
#             filtered_history.append(match)
#     return filtered_history


# def filter_by_champion(match_history, champion): #return filtered match history
#     filtered_history = []
#     game = 0
#     for match in match_history:
#         if(game == game_limit):
#             break
#         game +=1
#         p = match.participants[summoner]
#         if(p.champion.name == champ):
#             filtered_history.append(match)
#     return filtered_history

# def filter_by_keystone(match_history, keystone): #return filtered match history
#     filtered_history = []
#     game = 0
#     for match in match_history:
#         if(game == game_limit):
#             break
#         game +=1
#         p = match.participants[summoner]
#         if(p.runes.keystone.name == keystone):
#             filtered_history.append(match)
#     return filtered_history


# if(champ and keystone):
#     filtered_history = filter_by_both(history, champ, keystone)

# elif(champ):
#     filtered_history = filter_by_champion(history, champ)

# elif(keystone):
#     filtered_history = filter_by_keystone(history, keystone)

# else:
#     filtered_history = history


# for match in filtered_history:
#     p = match.participants[summoner]
#     if(p.team.win):
#         wins += 1
#     total_games += 1
# try:
#     winrate = (100 * (wins / total_games))
# except ZeroDivisionError:
#     print(f"You dont have any games playing {champ} using {keystone} in your last {game_limit} games")
# else:
#     print(f"Using {keystone} on {champ}, you have a {winrate}% winrate over {total_games} game(s), yayyyy")


"""

I'm such a fool
My code was trying to look through every single match in my match history, and tell me my winrate over my
entire league of legends career
I dont need to know that, bc it's probably low

"""


# import cassiopeia as cass

# f = open("api_key.txt", "r")
# api = f.read()
# f.close()

# cass.set_riot_api_key(api)  # This overrides the value set in your configuration/settings.

# summoner = cass.get_summoner(name="CanYouLimbo", region="NA")

# wins = 0
# total_games = 0
# game_limit = 17
# game = 0
# history = summoner.match_history


# for match in history:
#     p = match.participants[summoner]
#     if(p.team.win):
#         wins += 1
#     total_games += 1
#     game_limit = game_limit - 1
#     if(not game_limit):
#         break

# print((100 * (wins / total_games)))


"""
new and fixed!
I dont know what to say, but this data that im getting from Cass is outdated. 
its possibly three days old! im getting incorrect winrates over incorrect games
this is sad
i might have to use riot api by itself...
wish me luck i guess
but i will still use this for long term winrates, bc i think its actually really cool
as long as the games im trying to look at are more than 3 days old i guess ha ha

"""


import cassiopeia as cass
f = open("api_key.txt", "r")
api = f.read()
f.close()

# This overrides the value set in your configuration/settings.
cass.set_riot_api_key(api)

summoner = cass.get_summoner(name="CanYouLimbo", region="NA")

wins = 0
total_games = 0
game_limit = 10
game = 0
history = summoner.match_history
champ = input("Enter a champion (Enter nothing to look at all champs): ")
keystone = input("Enter a keystone (Enter nothing to look at all keystones): ")


def filter_by_both(match_history, champion, keystone):  # return filtered match history
    filtered_history = []
    game = 0
    for match in match_history:
        if (game == game_limit):
            break
        game += 1
        p = match.participants[summoner]
        if (p.runes.keystone.name == keystone and p.champion.name == champion):
            filtered_history.append(match)
    return filtered_history


def filter_by_champion(match_history, champion):  # return filtered match history
    filtered_history = []
    game = 0
    for match in match_history:
        if (game == game_limit):
            break
        game += 1
        p = match.participants[summoner]
        if (p.champion.name == champion):
            filtered_history.append(match)
    return filtered_history


def filter_by_keystone(match_history, keystone):  # return filtered match history
    filtered_history = []
    game = 0
    for match in match_history:
        if (game == game_limit):
            break
        game += 1
        p = match.participants[summoner]
        if (p.runes.keystone.name == keystone):
            filtered_history.append(match)
    return filtered_history


if (champ and keystone):
    filtered_history = filter_by_both(history, champ, keystone)

elif (champ):
    filtered_history = filter_by_champion(history, champ)

elif (keystone):
    filtered_history = filter_by_keystone(history, keystone)

else:
    filtered_history = history


for match in filtered_history:
    p = match.participants[summoner]
    if (game == game_limit):
        break
    game += 1
    if (p.team.win):
        wins += 1
    total_games += 1
try:
    winrate = (100 * (wins / total_games))
except ZeroDivisionError:
    print(
        f"You dont have any games playing {champ} using {keystone} in your last {game_limit} games")
else:
    print(
        f"Using {keystone} on {champ}, you have a {winrate}% winrate over {total_games} game(s), yayyyy")


"""

This is where I tried to make winrate into a separate function, which i think is a step in the right direction
but I can't get the total games to work, ill have to wait and see on this one

"""

# import cassiopeia as cass

# f = open("api_key.txt", "r")
# api = f.read()
# f.close()

# cass.set_riot_api_key(api)  # This overrides the value set in your configuration/settings.

# summoner = cass.get_summoner(name="CanYouLimbo", region="NA")

# wins = 0
# total_games = 0
# game_limit = 200
# game = 0
# history = summoner.match_history
# champ = input("Enter a champion (Enter nothing to look at all champs): ")
# keystone = input("Enter a keystone (Enter nothing to look at all keystones): ")


# def filter_by_both(match_history, champion, keystone): #return filtered match history
#     filtered_history = []
#     game = 0
#     for match in match_history:
#         print(game)
#         if(game == game_limit):
#             break
#         game +=1
#         p = match.participants[summoner]
#         if(p.runes.keystone.name == keystone and p.champion.name == champ):
#             print("found one")
#             filtered_history.append(match)
#     return filtered_history


# def filter_by_champion(match_history, champion): #return filtered match history
#     filtered_history = []
#     game = 0
#     for match in match_history:
#         if(game == game_limit):
#             break
#         game +=1
#         p = match.participants[summoner]
#         if(p.champion.name == champ):
#             filtered_history.append(match)
#     return filtered_history

# def filter_by_keystone(match_history, keystone): #return filtered match history
#     filtered_history = []
#     game = 0
#     for match in match_history:
#         if(game == game_limit):
#             break
#         game +=1
#         p = match.participants[summoner]
#         if(p.runes.keystone.name == keystone):
#             filtered_history.append(match)
#     return filtered_history

# def winrate(match_history):
#     wins = 0
#     total_games = 0
#     for match in match_history:
#         p = match.participants[summoner]
#         if(p.team.win):
#             wins += 1
#         total_games += 1
#     try:
#         return 100 * (wins / total_games)
#     except ZeroDivisionError:
#         return 0


# if(champ and keystone):
#     filtered_history = filter_by_both(history, champ, keystone)
#     winrate = winrate(filtered_history)


# elif(champ):
#     filtered_history = filter_by_champion(history, champ)
#     winrate = winrate(filtered_history)

# elif(keystone):
#     filtered_history = filter_by_keystone(history, keystone)
#     winrate = winrate(filtered_history)

# else:
#     winrate = winrate(history)


# print(f"Using {keystone} on {champ}, you have a {winrate}% winrate over {total_games} game(s), yayyyy")

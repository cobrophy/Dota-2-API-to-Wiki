import json
import urllib2
import datetime
import sys

# API key (This can be generated at http://steamcommunity.com/dev/apikey )

MyKey = ""

# Checking that there is a valid match id in the argument. (A sample match id is 19934308)

while True:
  try:
    MatchId = sys.argv[1]
    break
  except:
    print "Error: Argument required"
    print "You must enter a valid number for the match id."
    print "E.G. python DotaApiToWiki.py 12345678"
    sys.exit()
    
if len(MatchId) != 8:
  print "Error: Match Id wrong length"
  print "You must enter a valid number for the match id."
  print "E.G. python DotaApiToWiki.py 12345678"
  sys.exit()

# Generating URL and loading JSON

MatchDetailsUrl = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id="

Url = MatchDetailsUrl + str(MatchId) + "&key=" + MyKey

UrlData = urllib2.urlopen(Url).read()
MatchData = json.loads(UrlData)

# Assigning relevant JSON data to variables

JsonDate = MatchData[u'result'][u'starttime']
JsonWinner = MatchData[u'result'][u'radiant_win']

try:
  JsonRadiantTeam = MatchData[u'result'][u'radiant_name']
  JsonDireTeam = MatchData[u'result'][u'dire_name']
except KeyError:
  JsonRadiantTeam = ""
  JsonDireTeam = ""
  print "Note: No Team Names"

PlayerCount = MatchData[u'result'][u'human_players']
i = 0
RadiantTeam = {}
DireTeam = {}

while i < PlayerCount:
  PlayerName = MatchData[u'result'][u'players'][i][u'player_name']
  PlayerHero = MatchData[u'result'][u'players'][i][u'hero_id']
  if MatchData[u'result'][u'players'][i][u'player_slot'] < 10:
    RadiantTeam[PlayerName] = PlayerHero
  else:
    DireTeam[PlayerName] = PlayerHero
  i = i + 1

# Converting UNIX time to date time

WikiDate = datetime.datetime.fromtimestamp(JsonDate).strftime('%Y|%m|%d')

# Finding Winner

if JsonWinner == False:
  WikiResult = "<"
elif JsonWinner == True:
  WikiResult = ">"

# Hero Lookup for Hero Ids, may be some errors in here.

Url = "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?language=english&key=" + MyKey

UrlData = urllib2.urlopen(Url).read()
HeroData = json.loads(UrlData)

HeroCount = HeroData[u'result'][u'count']
j = 0
HeroLookup = {}
while j < HeroCount:
  HeroId = HeroData[u'result'][u'heroes'][j][u'id']
  HeroName = HeroData[u'result'][u'heroes'][j][u'localized_name']
  HeroLookup[HeroId] = HeroName 
  j = j + 1

# Converting Ids to Names

k = 0
while k < len(RadiantTeam.values()):
  TrialId = RadiantTeam.values()[k]
  TrialName = HeroLookup[TrialId]
  KeyName = RadiantTeam.keys()[k]
  RadiantTeam[KeyName] = TrialName
  k = k + 1

l = 0
while l < len(DireTeam.values()):
  TrialId = DireTeam.values()[l]
  TrialName = HeroLookup[TrialId]
  KeyName = DireTeam.keys()[l]
  DireTeam[KeyName] = TrialName
  l = l + 1

print RadiantTeam.items()
print DireTeam.items()

# Assigning Players and Heroes to Wiki Variables

if len(RadiantTeam) > 0:
  player1 = RadiantTeam.keys()[0]
  hero1 = RadiantTeam.values()[0]
else:
  player1 = ""
  hero1 = ""

if len(RadiantTeam) > 1:
  player2 = RadiantTeam.keys()[1]
  hero2 = RadiantTeam.values()[1]
else:
  player2 = ""
  hero2 = ""
  
if len(RadiantTeam) > 2:
  player3 = RadiantTeam.keys()[2]
  hero3 = RadiantTeam.values()[2]
else:
  player3 = ""
  hero3 = ""
  
if len(RadiantTeam) > 3:
  player4 = RadiantTeam.keys()[3]
  hero4 = RadiantTeam.values()[3]
else:
  player4 = ""
  hero4 = ""
  
if len(RadiantTeam) > 3:
  player5 = RadiantTeam.keys()[4]
  hero5 = RadiantTeam.values()[4]
else: 
  player5 = ""
  hero5 = ""

if len(DireTeam) > 0:
  player6 = DireTeam.keys()[0]
  hero6 = DireTeam.values()[0]
else:
  player6 = ""
  hero6 = ""

if len(DireTeam) > 1:
  player7 = DireTeam.keys()[1]
  hero7 = DireTeam.values()[1]
else:
  player7 = ""
  hero7 = ""
  
if len(DireTeam) > 2:
  player8 = DireTeam.keys()[2]
  hero8 = DireTeam.values()[2]
else:
  player8 = ""
  hero8 = ""
  
if len(DireTeam) > 3:
  player9 = DireTeam.keys()[3]
  hero9 = DireTeam.values()[3]
else:
  player9 = ""
  hero9 = ""
  
if len(DireTeam) > 3:
  player10 = DireTeam.keys()[4]
  hero10 = DireTeam.values()[4]
else: 
  player10 = ""
  hero10 = ""
  
# Generating unique file name for output
if len(JsonRadiantTeam) > 0:
  match = JsonRadiantTeam + ' v ' + JsonDireTeam
else:
  match = "Public Matchmaking"

filename = str(MatchId) + " - " + match

# Writing output to file

f = open(filename, 'w')
f.write(
'{{matchbox\n' +
'| date         = {{Start date|' + WikiDate + '|df=y}}\n' +
'| team1        = [[' + JsonRadiantTeam + ']]\n' +
'| score        = ' + WikiResult + '\n' +
'| team2        = [[' + JsonDireTeam + ']]\n' +
'| stadium      = \n' +
'<!-- Radiant Heroes -->\n' +
'| player1      = ' + player1 + '\n' +
'| hero1        = ' + hero1 + '\n' +
'| player2      = ' + player2 + '\n' +
'| hero2        = ' + hero2 + '\n' +
'| player3      = ' + player3 + '\n' +
'| hero3        = ' + hero3 + '\n' +
'| player4      = ' + player4 + '\n' +
'| hero4        = ' + hero4 + '\n' +
'| player5      = ' + player5 + '\n' +
'| hero5        = ' + hero5 + '\n' +
'<!-- Dire Heroes -->\n' +
'| player6      = ' + player6 + '\n' +
'| hero6        = ' + hero6 + '\n' +
'| player7      = ' + player7 + '\n' +
'| hero7        = ' + hero7 + '\n' +
'| player8      = ' + player8 + '\n' +
'| hero8        = ' + hero8 + '\n' +
'| player9      = ' + player9 + '\n' +
'| hero9        = ' + hero9 + '\n' +
'| player10     = ' + player10 + '\n' +
'| hero10       = ' + hero10 + '\n' +
'<!-- Replay -->\n' +
'| replay       = \n' +
'}}')
f.close()

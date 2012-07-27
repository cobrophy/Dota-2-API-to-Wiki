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
    print "You must enter a valid number for the match id."
    print "E.G. python DotaApiToWiki.py 12345678"
    sys.exit()
    
if len(MatchId) != 8:
  print "You must enter a valid number for the match id."
  print "E.G. python DotaApiToWiki.py 12345678"
  sys.exit()

if isinstance(MatchId, int) == False:
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
JsonRadiantTeam = MatchData[u'result'][u'radiant_name']
JsonDireTeam = MatchData[u'result'][u'dire_name']

JsonRadiant1Name = MatchData[u'result'][u'players'][0][u'player_name']
JsonRadiant1Hero = MatchData[u'result'][u'players'][0][u'hero_id']
JsonRadiant2Name = MatchData[u'result'][u'players'][1][u'player_name']
JsonRadiant2Hero = MatchData[u'result'][u'players'][1][u'hero_id']
JsonRadiant3Name = MatchData[u'result'][u'players'][2][u'player_name']
JsonRadiant3Hero = MatchData[u'result'][u'players'][2][u'hero_id']
JsonRadiant4Name = MatchData[u'result'][u'players'][3][u'player_name']
JsonRadiant4Hero = MatchData[u'result'][u'players'][3][u'hero_id']
JsonRadiant5Name = MatchData[u'result'][u'players'][4][u'player_name']
JsonRadiant5Hero = MatchData[u'result'][u'players'][4][u'hero_id']
JsonDire1Name = MatchData[u'result'][u'players'][5][u'player_name']
JsonDire1Hero = MatchData[u'result'][u'players'][5][u'hero_id']
JsonDire2Name = MatchData[u'result'][u'players'][6][u'player_name']
JsonDire2Hero = MatchData[u'result'][u'players'][6][u'hero_id']
JsonDire3Name = MatchData[u'result'][u'players'][7][u'player_name']
JsonDire3Hero = MatchData[u'result'][u'players'][7][u'hero_id']
JsonDire4Name = MatchData[u'result'][u'players'][8][u'player_name']
JsonDire4Hero = MatchData[u'result'][u'players'][8][u'hero_id']
JsonDire5Name = MatchData[u'result'][u'players'][9][u'player_name']
JsonDire5Hero = MatchData[u'result'][u'players'][9][u'hero_id']

# Converting UNIX time to date time

WikiDate = datetime.datetime.fromtimestamp(JsonDate).strftime('%Y|%m|%d')

# Finding Winner

if JsonWinner == False:
  WikiResult = "<"
elif JsonWinner == True:
  WikiResult = ">"

# Hero Lookup for Hero Ids, may be some errors in here.

HeroLookup = {
1:'Antimage', 
2:'Axe', 
3:'Bane', 
4:'Bloodseeker', 
5:'Crystal Maiden', 
6:'Drow Ranger', 
7:'Earthshaker', 
8:'Juggernaut', 
9:'Mirana', 
10:'Nevermore',
11:'Morphling',
12:'Phantom Lancer',
13:'Puck',
14:'Pudge',
15:'Razor',
16:'Sand King',
17:'Storm Spirit',
18:'Sven',
19:'Tiny',
20:'Vengeful Spirit',
21:'Windrunner',
22:'Zeus',
23:'Kunkka',
24:'',
25:'Lina',
26:'Lion',
27:'Shadow Shaman',
28:'Slardar',
29:'Tidehunter',
30:'Witch Doctor',
31:'Lich',
32:'Riki',
33:'Enigma',
34:'Tinker',
35:'Sniper',
36:'Necrolyte',
37:'Warlock',
38:'Beastmaster',
39:'Queen of Pain',
40:'Venomancer',
41:'Faceless Void',
42:'Skeleton King',
43:'Death Prophet',
44:'Phantom Assassin',
45:'Pugna',
46:'Templar Assassin',
47:'Viper',
48:'Luna',
49:'Dragon Knight',
50:'Dazzle',
51:'Rattletrap',
52:'Leshrac',
53:'Furion',
54:'Lifestealer',
55:'Dark Seer',
56:'Clinkz',
57:'Omniknight',
58:'Enchantress',
59:'Huskar',
60:'Night Stalker',
61:'Broodmother',
62:'Bounty Hunter',
63:'Weaver',
64:'Jakiro',
65:'Batrider',
66:'Chen',
67:'Spectre',
68:'Doom Bringer',
69:'Ancient Apparition',
70:'Ursa',
71:'Spirit Breaker',
72:'Gyrocopter',
73:'Alchemist',
74:'Invoker',
75:'Silencer',
76:'Obsidian Destroyer',
77:'Lycan',
78:'Brewmaster',
79:'Shadow Demon',
80:'Lone Druid',
81:'Chaos Knight',
82:'Meepo',
83:'Treant Protector',
84:'Ogre Magi',
85:'Undying',
86:'Rubick',
87:'Disruptor',
88:'Nyx Assassin',
89:'Naga Siren',
90:'Keeper of the Light',
91:'Wisp',
92:'Visage',
93:'Slark'}

# Converting Ids to Names

WikiRadiant1Hero = HeroLookup[JsonRadiant1Hero]
WikiRadiant2Hero = HeroLookup[JsonRadiant2Hero]
WikiRadiant3Hero = HeroLookup[JsonRadiant3Hero]
WikiRadiant4Hero = HeroLookup[JsonRadiant4Hero]
WikiRadiant5Hero = HeroLookup[JsonRadiant5Hero]
WikiDire1Hero = HeroLookup[JsonDire1Hero]
WikiDire2Hero = HeroLookup[JsonDire2Hero]
WikiDire3Hero = HeroLookup[JsonDire3Hero]
WikiDire4Hero = HeroLookup[JsonDire4Hero]
WikiDire5Hero = HeroLookup[JsonDire5Hero]

# Generating unique file name for output

filename = str(MatchId) + " - " + JsonRadiantTeam + ' v ' + JsonDireTeam

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
'| player1      = ' + JsonRadiant1Name + '\n' +
'| hero1        = ' + WikiRadiant1Hero + '\n' +
'| player2      = ' + JsonRadiant2Name + '\n' +
'| hero2        = ' + WikiRadiant2Hero + '\n' +
'| player3      = ' + JsonRadiant3Name + '\n' +
'| hero3        = ' + WikiRadiant3Hero + '\n' +
'| player4      = ' + JsonRadiant4Name + '\n' +
'| hero4        = ' + WikiRadiant4Hero + '\n' +
'| player5      = ' + JsonRadiant5Name + '\n' +
'| hero5        = ' + WikiRadiant5Hero + '\n' +
'<!-- Dire Heroes -->\n' +
'| player6      = ' + JsonDire1Name + '\n' +
'| hero6        = ' + WikiDire1Hero + '\n' +
'| player7      = ' + JsonDire2Name + '\n' +
'| hero7        = ' + WikiDire2Hero + '\n' +
'| player8      = ' + JsonDire3Name + '\n' +
'| hero8        = ' + WikiDire3Hero + '\n' +
'| player9      = ' + JsonDire4Name + '\n' +
'| hero9        = ' + WikiDire4Hero + '\n' +
'| player10     = ' + JsonDire5Name + '\n' +
'| hero10       = ' + WikiDire5Hero + '\n' +
'<!-- Replay -->\n' +
'| replay       = \n' +
'}}')
f.close()

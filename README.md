Dota-2-API-to-Wiki
==================

A Python script to generate wiki code for dota2wiki.com from a Dota 2 match id.

Setup: Adding your API key
==========================

To use you need to have your own API key, you can get this by going to http://steamcommunity.com/dev/apikey 
Enter any url as your domain, this is not tracked.

Open the python file in a text editor and add your API key to the line (inside the inverted commas):

MyKey = ""

Save the updated file.

Usage
=====

Requires Python 2.X 
Go to the folder containing the file in your terminal or command prompt, enter:

python DotaApiToWiki.py 12345678

Where 12345678 is the match id you want to generate wiki code for.
The match id can be found in the Dota 2 client at the top left of the scoreboard for any match.

Ticketed Tournaments
====================

My current understanding is that results for ticketed tournaments are only accessible via the api if you also have access through the client. i.e. you need a ticket tied to your account to get the results via the api.

Error 503 Service Temporarily Unavailable
=========================================

This sometimes happens with the API at the moment, simply try again or wait a few minutes and try again.
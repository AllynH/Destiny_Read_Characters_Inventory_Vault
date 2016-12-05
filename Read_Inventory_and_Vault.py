###################################################################################################
# Introduction:	This program does 2 things:
#				1. Reads a characters equipped items and prints them to the screen.
#				2. Reads a your vault contents and creates a HTML page displaying the name, description, and image for each item in your vault.
#
# Important:
#				In order to make this program work you'll need to add your username, password, api_key, destinyMembershipId and characterId in the Header_file.py
#				For more details view the full blog post: http://allynh.com/blog/creating-a-python-app-for-destiny-part-5-reading-a-characters-inventory-and-vault-contents/
#				For details on how to log into PSN view this blog post: http://allynh.com/blog/creating-a-python-app-for-destiny-part-3-logging-in-to-bungie-net-and-authenticating-with-psn/
#
# Usage:		python equipItem.py
# Created by:	Allyn Hunt - www.AllynH.com
###################################################################################################

from Header_file import *
from PSN_login import login
from Inventory_Management import *
import requests
import json
import sqlite3
import pickle #Optional

# Read in a template HTML file:
template_file = open('template.html', "r")
my_html = template_file.read()
template_file.close()

# Open our Destiny Manifest:
with open('item.pickle', 'rb') as data:
	all_data = pickle.load(data)

# Uncomment this line to print JSON output to a file:
#f = open('output.txt', 'w')

# Log in via PSN and create our persistant HTTP session: 
session = requests.Session()
session = login(username, password, api_key)

# Print character inventory items to the screen:
getCharacterInventory(session, characterId)

# Print vault contents to a file called "Vault_contents.html":
vaultResult = getVault(session)
my_html = my_html + parseVaultHtml(session, vaultResult, all_data)

# Create our output file and copy in the HTML from our template:
my_outfile = open('Vault_contents.html', 'w')
my_outfile.write(my_html.encode("utf-8"))


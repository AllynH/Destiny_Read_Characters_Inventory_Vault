###################################################################################################
# Important:
#				In order to make this program work you'll need to add your username, password, api_key, destinyMembershipId and characterId in the Header_file.py
#				For more details view the full blog post: http://allynh.com/blog/creating-a-python-app-for-destiny-part-5-reading-a-characters-inventory-and-vault-contents/
#				For details on how to log into PSN view this blog post: http://allynh.com/blog/creating-a-python-app-for-destiny-part-3-logging-in-to-bungie-net-and-authenticating-with-psn/
#
# Usage:		python equipItem.py
# Created by:	Allyn Hunt - www.AllynH.com
###################################################################################################
# PSN Username:
username = emailaddr
password = mypassword
api_key = API_KEY

# Destiny API X-Key:
API_KEY = ""
HEADERS = {"X-API-Key": API_KEY}

# Destiny parameters:
membershipType = "2" # PS4 = 2
destinyMembershipId = ""

characterId 		= ""
characterId_Warlock	= ""
characterId_Titan 	= ""
characterId_Hunter 	= ""

characterHash = {
	'Warlock':'',
	'Titan':'',
	'Hunter':''
}

# URL Builder:
base_url = "https://www.bungie.net/platform/Destiny/"

# Vendor details:
vendorHash = {
	'1821699360': 'Future_War_Cult',
	'1808244981': 'New_Monarchy',
	'3611686524': 'Dead_Orbit',
	'242140165': 'Iron_Banner'
}

vendorId_FWC	= "1821699360"	# Future War Cult
vendorId_NM		= "1808244981"	# New Monarchy
vendorId_DO		= "3611686524"	# Dead Orbit
vendorId_IB		= "242140165"	# Iron Banner

# Vault size:
vaultArmour = 108
vaultWeapons = 108
vaultInventory = 72
vaultSize = vaultArmour + vaultWeapons + vaultInventory

###################################################################################################
# Introduction:	This program starts the foundation for an inventory management system - by doing 2 things:
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

from PSN_login import login
import requests
import json

def transferItem(payload, session):
	req_string = base_url + "TransferItem/"
	print "Transferring item from vault to character..."
	res = session.post(req_string, data=payload)
	error_stat = res.json()['ErrorStatus'].decode('utf-8')
	print "Error status: " + error_stat + "\n"
	return res

def equipItem(payload, session):
	# Send the request to equip the item:
	equip_url = base_url + "EquipItem/"
	print "Equipping item..."
	res = session.post(equip_url, data=payload)
	error_stat = res.json()['ErrorStatus'].decode('utf-8')
	print "Error status: " + error_stat + "\n"
	return res

def getVault(session):
	getVault_url = base_url + membershipType + "/MyAccount/Vault/"
	res = session.get(getVault_url, params={'accountId': destinyMembershipId})
	print (res.url)
	error_stat = res.json()['ErrorStatus'].decode('utf-8')
	print "Error status: " + error_stat + "\n"
	#print (res.status_code)
	#print (res.text)
	return res

	
def getCharacterInventory(session, charId):
	req_string = base_url + membershipType + "/Account/" + destinyMembershipId + "/Character/" + charId + "/Inventory"
	print "Fetching data for: " + req_string + "\n"
	res = session.get(req_string)
	error_stat = res.json()['ErrorStatus']
	print "Error status: " + error_stat + "\n"
	return res

def parseVault(session, vaultResult, all_data):
	array_size = 0
	weapon_list = [{
		"membershipType": 2,
		"itemReferenceHash": 0,
		"itemId": 0,
		"characterId": characterId_Warlock,
		"stackSize": 1,
		"transferToVault": False
	} for array_size in range(vaultSize)]
	array_size = 0

	for bucket in vaultResult.json()['Response']['data']['buckets']:
	#f.write (json.dumps(bucket['items'], indent=4))
		for item in bucket['items']:
			hashReqString = base_url + "Manifest/6/" + str(item['itemHash'])
			weapon_list[array_size]['itemReferenceHash'] = item['itemHash']
			weapon_list[array_size]['itemId'] = item['itemInstanceId']
			inventoryItem = all_data['DestinyInventoryItemDefinition'][item['itemHash']]
			item_name = inventoryItem['itemName']
			item_tier = inventoryItem['tierTypeName']
			item_type = inventoryItem['itemTypeName']
			item_icon = inventoryItem['icon']
			print "Item name is: " + item_name
			array_size += 1
		
	return weapon_list

def parseVaultHtml(session, vaultResult, all_data):
	my_html = ""
	array_size = 0
	weapon_list = [{
		"membershipType": 2,
		"itemReferenceHash": 0,
		"itemId": 0,
		"characterId": characterId_Warlock,
		"stackSize": 1,
		"transferToVault": False
	} 
	for array_size in range(vaultSize)]
	array_size = 0

	for bucket in vaultResult.json()['Response']['data']['buckets']:
		for item in bucket['items']:
			inventoryItem = all_data['DestinyInventoryItemDefinition'][item['itemHash']]
			item_name = inventoryItem['itemName']
			item_tier = inventoryItem['tierTypeName']
			item_type = inventoryItem['itemTypeName']
			item_icon = "http://www.bungie.net/" + inventoryItem['icon']
			print "Item name is: " + item_name
			array_size += 1
			print "Item is: " + item_name
			print "Item type is: " + item_tier + " " + item_type + "\n"
			my_html = my_html + "\t\t<div class=\"col-md-4\">\n"
			my_html = my_html + "\t\t\t<div class=\"thumbnail\">\n"
			my_html = my_html + "\t\t\t\t<a href=\"" + item_icon + "\">\n"
			my_html = my_html + "\t\t\t\t<img src=\"" + item_icon + "\">\n"
			my_html = my_html + "\t\t\t\t</a>\n"
			my_html = my_html + "\t\t\t\t<h3>" + item_name + "</h3>\n"
			my_html = my_html + "\t\t\t\t<p>" + item_tier + " " + item_type + "</p>\n"
			my_html = my_html + "\t\t\t</div>\n"
			my_html = my_html + "\t\t</div>\n"
		
	# Close the HTML file:
	my_html = my_html + "\t</div> <!-- row -->\n"
	my_html = my_html + "\t</div> <!-- container -->\n"
	my_html = my_html + "</div> <!-- inventory-container -->\n"
	my_html = my_html + "</body>\n"
	my_html = my_html + "</html>\n"
	return my_html

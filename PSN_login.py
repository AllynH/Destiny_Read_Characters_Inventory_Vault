###################################################################################################
# Introduction:	This function is used to log into Bungie.net via PSN.
#				For more details view the full blog post: http://allynh.com/blog/creating-a-python-app-for-destiny-part-3-logging-in-to-bungie-net-and-authenticating-with-psn/
#
# Notes:		To use this you'll need:
#					Your PSN log in details - username and password.
#					Your Bungie.net API-Key
#				Please read the blog post for more information
#
# Usage:		session = login(username, password, api_key)
# Created by:	This program was created with the contribution of many people on destinydevs.github.io and the Bungie forum: 
#				http://destinydevs.github.io/BungieNetPlatform/docs/Authentication
#				https://www.bungie.net/en/Clan/Post/39966/215947676/0/0
#				Allyn Hunt - www.AllynH.com
###################################################################################################
import requests
import json
import logging
from base64 import b64encode
from urlparse import urlparse
import httplib
httplib.HTTPConnection.debuglevel = 0

def login(username, password, api_key):
	################################################
	BUNGIE_SIGNIN_URI = "https://www.bungie.net/en/User/SignIn/Psnid"
	PSN_OAUTH_URI = "https://auth.api.sonyentertainmentnetwork.com/login.do"

	request1 = requests.get(BUNGIE_SIGNIN_URI, allow_redirects=True)
	jsessionid0 = request1.history[1].cookies["JSESSIONID"]
	params = urlparse(request1.url).query
	params64 = b64encode(params)
	# Post credentials and pass the JSESSIONID cookie.
	# We get a new JSESSIONID cookie.
	# Note: It doesn't appear to matter what the value of `params` is, but
	# we'll pass in the appropriate value just to be safe.
	post = requests.post(
		PSN_OAUTH_URI,
		data={"j_username": username, "j_password": password, "params": params64},
		cookies={"JSESSIONID": jsessionid0},
		params={"redirect_uri": BUNGIE_SIGNIN_URI},
		allow_redirects=False
	)

	#print "Post URL"
	#print post.url

	if "authentication_error" in post.headers["location"]:
		print("Invalid credentials")
	#	return None

	jsessionid1 = post.cookies["JSESSIONID"]
	#print("JSESSIONID: %s", jsessionid1)

	session = requests.Session()

	# Follow the redirect from the previous request passing in the new
	# JSESSIONID cookie. This gets us the Bungie cookies.
	session.get(
		post.headers["location"],
		allow_redirects=True,
		cookies={"JSESSIONID": jsessionid1}
	)

	# Add the API key to the current session
	session.headers["X-API-Key"] = api_key
	session.headers["x-csrf"] = session.cookies["bungled"]
	#session.cookies.update({"bungleatk": session.cookies["bungleatk"], "bungled": session.cookies["bungled"], "bungledid": session.cookies["bungledid"]})

	#print (str(session.cookies))
	#return session
	#print "Grabbing cookies..."

	####################################################################################

	return session
import datetime
import pdb
import httplib
import optparse
import urllib
import urllib2
import oauth2
import json

auth = {
	'consumer_key': '7BQorpwcEYvhcplPz7bPjA', 
	'consumer_secret': 'Haj-cF4_gz3eYCP4k6AGWML8Vu8',
	'access_token': '54nsx5KN1O6undGlE1qKUhrZPgdlYRQD',
	'access_token_secret': 'Ym4Lt4sFZfh4zFXRixbfb56QKUE'
}

base_url = 'http://api.yelp.com/v2/search'
http_method = 'GET'

def get_results(search_params, location):
	respArr = []

	for search_param in search_params:
		url_params = {}
		url_params['location'] = location
		url_params['term'] = search_param
		respArr.append(request(url_params))
	
	return respArr

def request(url_params):
	encoded_params = urllib.urlencode(url_params)
	url = '%s?%s' % (base_url, encoded_params)
	# print 'URL: %s' % url

	# Oauth Sign
	consumer = oauth2.Consumer(auth['consumer_key'],
							   auth['consumer_secret'])
	oauth_request = oauth2.Request('GET', url, {})
	oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
						  'oauth_timestamp': oauth2.generate_timestamp(),
						  'oauth_token': auth['access_token'],
						  'oauth_consumer_key': auth['consumer_key']})
	token = oauth2.Token(auth['access_token'],
						 auth['access_token_secret'])
	oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
	signed_url = oauth_request.to_url()
	# print 'Signed URL: %s\n' % (signed_url)

	# Connect
	try:
		conn = urllib2.urlopen(signed_url, None)
		try:
			response = conn.read()
		finally:
			conn.close()
	except urllib2.HTTPError, error:
		response = ""

	return response

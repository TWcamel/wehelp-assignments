import urllib.request as req
import json

def get(url):
	with req.urlopen(url) as response:
		return json.load(response)


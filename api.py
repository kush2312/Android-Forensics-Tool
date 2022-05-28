from email import message
import requests
import urllib.parse
import validators
import requests
import json
import json
from bs4 import BeautifulSoup

message = '<p>Hi</p>'
soup = BeautifulSoup(message, 'html.parser')

a = soup.find('a') 

if a:
    url = a['href']
    print(url)

else:
    print("Here")

parsed = urllib.parse.quote(url, safe='')
print(parsed)

api = "https://ipqualityscore.com/api/json/url/" + "vKb0lHRVThz0TCnZ84qGLqOHaFl5W0pi" + "/" + parsed
response = requests.get(api)
response_json = json.loads(response.content)
ip_address = response_json.get('ip_address', "")
suspicious = response_json.get('suspicious', "")
malware = response_json.get('malware', "")
phishing = response_json.get('phishing', "")
risk_score = response_json.get('risk_score', "")

# print(response.content)


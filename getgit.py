#!/usr/local/bin/python3

import http.client,ssl,json,argparse

plus=x=0

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--query", help="Search Terms", action="store", dest="query")
parser.add_argument("-l", "--language", help="language to search for", action="store", dest="language")
parser.add_argument("-s", "--stars", help="minimum number of stars", action="store", dest="stars")
parser.add_argument("-u", "--user", help="user name", action="store", dest="user")
args = parser.parse_args()

conn = http.client.HTTPSConnection('api.github.com', context=ssl._create_unverified_context())
url='/search/repositories?q='
starsurl='stars:>='
language='language:'
user='user:'

endurl='&sort=stars&order=desc&per_page=100'

if args.query:
	url = url + args.query
	plus=1
if args.language:
	if plus:
		url = url + "+"
	url = url + language + args.language
	plus=1
if args.stars:
	if plus:
		url = url + "+"
	url = url + starsurl + args.stars
	plus=1
if args.user:
	if plus:
		url = url + "+"
	url = url + user + args.user

url=url+endurl
method = 'GET'
headers = {"Accept": "image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-powerpoint, application/vnd.ms-excel, application/msword, application/x-shockwave-flash, */*", "Accept-Language": "en-us", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MANM; rv:11.0) like Gecko", "Connection": "Keep-Alive"}

conn.request(method, url, None, headers)

httpResponse = conn.getresponse()

response_dict=json.loads(httpResponse.read())

print ('Results of getgit query.......')

count=len(response_dict['items'])

while x < len(response_dict['items']):
	print ('Full Name: ' + response_dict['items'][x]['full_name'])
	print ('Owner: ' + response_dict['items'][x]['owner']['login'])
	print ('Owner Type: ' + response_dict['items'][x]['owner']['type'])
	print ('Html Url: ' + response_dict['items'][x]['html_url'])
	if response_dict['items'][x]['description']:
		print ('Description: ' + response_dict['items'][x]['description'])
	print ('Number of Watchers: ' + str(response_dict['items'][x]['watchers']))
	if response_dict['items'][x]['language']:
            print ('Language: ' + response_dict['items'][x]['language'])
	print ('Number of Stars: ' + str(response_dict['items'][x]['stargazers_count']))
	print ('Created at: ' + response_dict['items'][x]['created_at'])
	print ('Size: ' + str(response_dict['items'][x]['size']))
	print ('Open Issues Count: ' + str(response_dict['items'][x]['open_issues_count']))
	print ('----------------------------------')
	x=x+1
print ('Total number of results: ' + str(count))

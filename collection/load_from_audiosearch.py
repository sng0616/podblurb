#import os
import sys
#import requests
#import json
import passwords as p

#from collection.models import podcast_show
from audiosearch import Client

show_title_search = ' '.join(sys.argv[1:])

print show_title_search

c = Client(p.audiosearch_oauth_id, p.audiosearch_oauth_secret)

show_info = c.search({ 'q': show_title_search}, 'shows')

print show_info
#import json
import passwords as p
import math as m

#from collection.models import podcast_show
from audiosearch import Client


c = Client(p.audiosearch_oauth_id, p.audiosearch_oauth_secret)

results = c.search({ 'q': '*'}, 'shows')

total_pages = int(m.floor(results['total_results']/results['results_per_page']))

print results['total_results'], total_pages

all_shows = []

#with open('audiosearch_json_file.txt', 'wb') as audio:
for page in range(400,(total_pages+1)):
    print page
#        audio.write(str(page)+'\n')
    page_results = c.search({ 'q': '*', 'page': page}, 'shows')
    for i in page_results['results']:
        if i['title'] not in all_shows:
            all_shows.append(i['title'])
#                audio.write(i['title']+'\n')
            print i['title']
        else:
            pass
        


#all_shows = sorted(all_shows)
##
#print all_shows[0:15]
print len(all_shows)

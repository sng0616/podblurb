#import json
import passwords as p
import math as m

#from collection.models import podcast_show
from audiosearch import Client


c = Client(p.audiosearch_oauth_id, p.audiosearch_oauth_secret)

results = c.search({ 'q': '*'}, 'shows')

total_pages = int(m.floor(results['total_results']/results['results_per_page']))

#print results['total_results'], total_pages

all_shows = []

for page in range(1,(total_pages+1)):
#for page in range(1,5):
#    print page
    try:
        page_results = c.search({ 'q': '*', 'page': page}, 'shows')
        for i in page_results['results']:
            if i['title'] not in all_shows:
                show = [str(i['title'])]
                show_string = tuple(show,)+tuple(show,)
                all_shows.append(show_string)
#                print i['title']
            else:
                pass
    except ValueError:
        pass
        
all_shows = sorted(all_shows)
#print all_shows[:5]
#print len(all_shows)

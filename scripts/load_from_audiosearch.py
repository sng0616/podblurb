#import json
import passwords as p
import math as m
import os
import sys

project_path = '/media/removable/UNTITLED/podblurb/'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'podblurb.settings')
sys.path.append(project_path)

os.chdir(project_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.core import serializers as s
from collection.models import podcast_show
#from django.contrib.auth.models import User
from audiosearch import Client


c = Client(p.audiosearch_oauth_id, p.audiosearch_oauth_secret)

results = c.search({ 'q': '*'}, 'shows')

total_pages = int(m.floor(results['total_results']/results['results_per_page']))

#print results['total_results'], total_pages

all_shows = []

#for page in range(1,(total_pages+1)):
for page in range(1,5):
#    print page
    try:
        page_results = c.search({ 'q': '*', 'page': page}, 'shows')
        for i in page_results['results']:
            if i['title'] not in all_shows:
#                show = [str(i['title'])]
#                show_string = tuple(show,)+tuple(show,)
                show = {'id':i['id'],'title':i['title'],'description':i['description'],'website':i['rss_url'], 'show_tags':i['categories']} 
                all_shows.append(show)
#                print i['title']
            else:
                pass
    except ValueError:
        pass
        
#all_shows = sorted(all_shows)
print all_shows
#print len(all_shows)

#users = User.objects.all()

#if __name__ == "__main__":
#    for i in range(0,len(all_shows)):
#        show_model = podcast_show(show_name = choice(all_shows))
#        show_model.save()

class podcast_show_serializer(s.ModelSerializer):
    class Meta:
        model = podcast_show
        
data_serializer = podcast_show_serializer(data = all_shows, many = True)
if data_serializer.is_valid():
    data_serializer.save()

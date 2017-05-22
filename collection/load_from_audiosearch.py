#import os
#import sys
import requests
import json
import passwords as p

from collection.models import podcast_show
from audiosearch import Client

c = Client(p.audiosearch_oauth_id, p.audiosearch_oauth_secret)


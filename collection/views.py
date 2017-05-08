from django.shortcuts import render
from collection.models import podcast_show

# Create your views here.
#def index(request):
#    return render(request,'index.html')

def index(request):
    podcast = 'my favorite read'
    number = 7
#    shows = podcast_show.objects.filter(name__contains = 'popular').order_by('name')
    shows = podcast_show.objects.all().order_by('id').reverse()
    return render(request, 'index.html', {
        'pdc':podcast, 
        'num':number,
        'podcasts':shows
    })

def show_detail(request, slug):
    # Get object
    select_show = podcast_show.objects.get(slug=slug)
    # Pass object to template
    return render(request, 'shows/show.html', {'sshow':select_show})
    
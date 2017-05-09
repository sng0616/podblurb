from django.shortcuts import render, redirect
from collection.forms import EditForm
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

def show_edit(request, slug):
    select_show = podcast_show.objects.get(slug=slug)
    form_class = EditForm
    
    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # Get data from submitted form 
        form = form_class(data = request.POST, instance = select_show)
        
        if form.is_valid():
            form.save()
            return redirect('show', slug=select_show.slug)
        
    else:
        form = form_class(instance = select_show)
    return render(request, 'shows/edit.html', {
        'form':form,
        'sshow':select_show
    })
        
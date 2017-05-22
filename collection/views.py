from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import Http404
from django.db.models import Q

from collection.forms import EditForm
from collection.models import podcast_post, podcast_show

import operator

# Create your views here.
#def index(request):
#    return render(request,'index.html')

def index(request):
    podcast = 'my favorite read'
    number = 7
#    shows = podcast_post.objects.filter(post_title__contains = 'popular').order_by('post_title')
    shows = podcast_post.objects.all().order_by('id').reverse()
    
    query_name = request.GET.get("query")
    
    if query_name:
        query_list = query_name.split()
        result = shows.filter(
            reduce(operator.and_, (Q(post_title__icontains=q) for q in query_list)) |
            reduce(operator.and_, (Q(post_content__icontains=q) for q in query_list))
#            reduce(operator.and_, (Q(tags__icontains=q) for x in tags for q in query_list))
        )
        return render(request, 'index.html', {
            'q':query_name,
            'post_list':result,
            'pdc':podcast, 
            'num':number, 
        }) 
    else:
        return render(request, 'index.html', {
            'pdc':podcast, 
            'num':number,
            'podcasts':shows
        })

def show_detail(request, slug):
    # Get object
    select_show = podcast_post.objects.get(slug=slug)
    # Pass object to template
    return render(request, 'shows/show.html', {'sshow':select_show})

@login_required
def show_edit(request, slug):
    select_show = podcast_post.objects.get(slug=slug)
    
    if select_show.user != request.user:
        raise Http404
    
    form_class = EditForm
    
    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # Get data from submitted form 
        form = form_class(data = request.POST, instance = select_show)
        
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect('show', slug=select_show.slug)
        
    else:
        form = form_class(instance = select_show)
    return render(request, 'shows/edit.html', {
        'form':form,
        'sshow':select_show
    })

def create_post(request):
    form_class = EditForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.slug = slugify(post.post_title)
            post.save()
            post.save_m2m()
            
            return redirect('show',slug=post.slug)
    else:
        form = form_class()
    return render(request, 'shows/create_post.html', {'form' : form})

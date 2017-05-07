from django.shortcuts import render

# Create your views here.
#def index(request):
#    return render(request,'index.html')

def index(request):
    # Define a variable to appear on the home page
    podcast = 'my favorite murder'
    number = 7
    return render(request,'index.html',{'pc' : podcast, 'num' : number,})
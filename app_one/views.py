from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        "date": strftime("%B %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request,'index.html', context)
from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime()),
    }
    return render(request, 'time_display/index.html', context)

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def polls(request):
    msg = "<h1>Beyond the Great Wall, we can reach any corner of the world.</h1>"
    return HttpResponse(msg)


def about(request):
    return render(request, 'polls/about.html')


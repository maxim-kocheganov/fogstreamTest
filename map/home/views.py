from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def homeView(request):
    html = '<html><body>Home</body></html>'
    return HttpResponse(html)
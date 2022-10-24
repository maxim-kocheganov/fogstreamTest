from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def uploadCSV(request):
    html = '<html><body>Test</body></html>'
    return HttpResponse(html)
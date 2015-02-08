from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import requests

def new(request):
    return render(request, 'dashboard.html')

def watson(request):
	r = requests.post(watson_url, data=requeset.data, headers=request.headers)

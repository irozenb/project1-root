from django.http import HttpResponse
from django.shortcuts import render
def about(request):
	return HttpResponse('About')
def home(request):
	return render(request, 'home.html', {'hello':'Hello'})
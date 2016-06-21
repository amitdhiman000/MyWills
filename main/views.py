from django.shortcuts import render

# Create your views here.

def home(request):
	data = {'title':'Home'}
	return render(request, 'home.html', data)

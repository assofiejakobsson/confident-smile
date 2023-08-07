from django.shortcuts import render

# index function to handle requests to the home page
def index(request):
    
    return render(request, 'home/index.html')
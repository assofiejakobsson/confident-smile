from django.shortcuts import render, redirect
from .forms import NewsletterUserForm


# Create your views here.

def index(request):

    form = NewsletterUserForm()

    return render(request, 'home/index.html', {'form': form})



def subscribe(request):
    if request.method == 'POST':
        form = NewsletterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = NewsletterUserForm()
    return render(request, 'home/index.html', {'form': form}) 



    
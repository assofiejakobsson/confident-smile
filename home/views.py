from django.shortcuts import render, redirect
#from .forms import NewsletterUserForm
#from django.contrib import messages


def index(request):

    return render(request, 'home/index.html')




""" def index(request):

    form = NewsletterUserForm()

    return render(request, 'home/index.html', {'form': form}) """


""" 
def subscribe(request):
    if request.method == 'POST':
        form = NewsletterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully subscribed to the newsletter!')
            return redirect('home:home')
    else:
        form = NewsletterUserForm()
    return render(request, 'home/index.html', {'form': form}) """



    
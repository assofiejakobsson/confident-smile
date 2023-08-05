from .models import FAQ

def faqs(request):
    faqs = FAQ.objects.all()
    return {'faqs': faqs}
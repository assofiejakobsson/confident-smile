from django.shortcuts import get_object_or_404, render
from .models import FAQ


def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'siteinfo/faq_list.html', {'faqs': faqs})

def faq_detail(request, faq_id):
    faq = get_object_or_404(FAQ, pk=faq_id)
    return render(request, 'siteinfo/faq_detail.html', {'faq': faq})


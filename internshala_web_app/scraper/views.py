from django.shortcuts import render

from backend.src.utils import Utils


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def scraper(request):
    keywords = Utils.get_available_keywords()
    return render(request, 'services-scraping_website.html', {'keywords': keywords})


def analytics(request):
    return render(request, 'services-analytics.html')


def download(request):
    return render(request, 'download.html')

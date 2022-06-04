from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def scraper(request):
    return render(request, 'services-scraping_website.html')


def analytics(request):
    return render(request, 'services-analytics.html')


def download(request):
    return render(request, 'download.html')

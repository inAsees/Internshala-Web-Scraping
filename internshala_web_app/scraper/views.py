import os

from django.shortcuts import render, redirect

from backend.src.scrapper import ScrapInternshala
from backend.src.utils import Utils
from output_file_path import dir_name


# Create your views here.
def index(request):
    if request.method == "GET":
        categories = Utils.get_categories()
        return render(request, 'index.html', {'categories': categories})
    category = Utils.get_url_encoded_data(request.POST['categories'])
    scrap_internshala = ScrapInternshala(category)
    scrap_internshala.scrap_all_pages()
    file_path = os.path.join(dir_name, 'internshala_web_app/scraper/static/scraper/output.csv')
    scrap_internshala.dump(file_path)
    return redirect(download)


def download(request):
    return render(request, 'download.html')

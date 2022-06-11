import os
from django.shortcuts import render, redirect
from backend.src.scrapper import ScrapInternshala
from backend.src.utils import Utils
from output_file_path import dir_name

# Create your views here.
def index(request):
    if request.method == "GET":
        keywords = Utils.get_available_keywords()
        return render(request, 'index.html', {'keywords': keywords})
    keyword_search = request.POST['keyword']
    scrap_internshala = ScrapInternshala(keyword_search)
    scrap_internshala.scrap_all_pages()
    file_path = os.path.join(dir_name, 'internshala_web_app/scraper/static/scraper/output.csv')
    scrap_internshala.dump(file_path)
    return redirect(download)


def download(request):
    return render(request, 'download.html')

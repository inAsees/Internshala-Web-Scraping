from django.shortcuts import render
from backend.src.scrapper import ScrapInternshala
from backend.src.utils import Utils
from .models import InternshipDetail


# Create your views here.
def index(request):
    if request.method == "GET":
        keywords = Utils.get_available_keywords()
        return render(request, 'index.html', {'keywords': keywords})
    keyword_search = request.POST['keyword']
    scrap_internshala = ScrapInternshala(keyword_search)
    scrap_internshala.scrap_all_pages()
    for d in scrap_internshala.get_company_info_list():
        intern = InternshipDetail(internship_id=d.internship_id, title=d.job_title, company=d.company,
                                  monthly_stipend=d.monthly_lump_sum, weekly_stipend=d.weekly_lump_sum,
                                  incentives=d.incentive, duration=d.duration_in_days, location=d.location,
                                  last_date_to_apply=d.apply_by, applicants_count=d.applicants,
                                  number_of_openings=d.number_of_openings, skills=d.skill_set, perks=d.perks,
                                  src_url=d.src_url)
        intern.save()
    return render(request, 'index.html')

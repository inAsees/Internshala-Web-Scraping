from django.db import models


class InternshipDetail(models.Model):
    internship_id = models.IntegerField()
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    monthly_stipend = models.IntegerField()
    weekly_stipend = models.IntegerField()
    incentives = models.CharField(max_length=200)
    duration = models.IntegerField()
    location = models.CharField(max_length=100)
    last_date_to_apply = models.DateField()
    applicants_count = models.IntegerField()
    number_of_openings = models.IntegerField()
    skills = models.CharField(max_length=300)
    perks = models.CharField(max_length=300)
    src_url = models.CharField(max_length=300)
    status = models.CharField(max_length=50)

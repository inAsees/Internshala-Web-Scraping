from django.db import models


class InternshipDetail(models.Model):
    internship_id = models.IntegerField()
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    monthly_stipend = models.IntegerField(null=True)
    weekly_stipend = models.IntegerField(null=True)
    incentives = models.CharField(max_length=200, blank=True)
    duration = models.IntegerField()
    location = models.CharField(max_length=100)
    last_date_to_apply = models.DateField(null=True)
    applicants_count = models.IntegerField()
    number_of_openings = models.IntegerField(null=True)
    skills = models.CharField(max_length=300, blank=True)
    perks = models.CharField(max_length=300, blank=True)
    src_url = models.CharField(max_length=300)
    status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

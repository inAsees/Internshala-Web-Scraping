# Generated by Django 4.0.5 on 2022-06-04 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internshipdetail',
            old_name='openings',
            new_name='number_of_openings',
        ),
    ]

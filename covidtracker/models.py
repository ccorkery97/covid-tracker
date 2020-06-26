from django.db import models
import csv

# Create your models here.
class State(models.Model):
    date = models.CharField(max_length=100)
    name = models.CharField(max_length=100) #state (initials)
    positive = models.CharField(max_length=100) 
    negative = models.CharField(max_length=100)
    deaths = models.CharField(max_length=100)
    hospitalized = models.CharField(max_length=100)



with open('./daily.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        State(date=row['date'], name=row['state'], positive=row['positive'], negative=row['negative'], deaths=row['death'], hospitalized=row['hospitalized']).save()
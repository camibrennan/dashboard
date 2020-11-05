from django.db import models

# Create your models here.
class Discogs(models.Model):
    Artist = CharField(max_length = 100)
    Title = CharField(max_length = 100)
    Label = CharField(max_length = 100)
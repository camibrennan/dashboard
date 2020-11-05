from django.shortcuts import HttpResponse 
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd 
import requests
import csv
import pygal

def github_api(request):
    response = requests.get('https://api.github.com/users/camibrennan/repos')
    repo_list = response.json()

    chart = pygal.Pie()
    for repo_dict in repo_list:
        value = repo_dict["id"]
        label = repo_dict["name"]
        chart.add(label, value)

    chart_svg = chart.render()
    context = {
        "rendered_chart_svg": chart_svg,
    }

    return render(request, 'github.html', context)

def open_csv(): 
    discogs = open("discogs/discogs.csv")
    for row in csv.DictReader(discogs):
        return("Album Info:", row['Artist'],row['Title'],row['Label'], row['Format'],)

def all_albums(request):
    album_info = open_csv()
    context = {
    "discogs_list": album_info,
    }
    return render(request,"all_albums.html", context)




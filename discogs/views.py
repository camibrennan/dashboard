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
        value = repo_dict["size"]
        label = repo_dict["name"]
        chart.add(label, value)

    chart_svg = chart.render()
    context = {
        "rendered_chart_svg": chart_svg,
    }

    return render(request, 'github.html', context)

def open_csv(): 
    discogs = open("discogs/discogs.csv")
    album_list = []
    for row in csv.DictReader(discogs):
        album_list.append({
        "Artist": row['Artist'],
        "Title": row['Title'],
        "Label": row['Label'], 
        "Format": row['Format'],
        "Release Year": row["Released"], #TODO NUMBER OR STRING
        })
    return album_list   
           

def all_albums(request):
    album_info = open_csv()
    context = {
    "discogs_list": album_info,
    }
    return render(request,"all_albums.html", context)




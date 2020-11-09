from django.shortcuts import HttpResponse 
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd 
import requests
import csv
import pygal
from .models import DashboardPanel

def github_api(request):
    response = requests.get('https://api.github.com/users/camibrennan/repos')
    repo_list = response.json()

    chart = pygal.Pie()
    chart.title = 'GitHub Repositories by Size'
    for repo_dict in repo_list:
        value = repo_dict["size"]
        label = repo_dict["full_name"]
        chart.add(label, value)
    chart_svg = chart.render()

    context = {
        "rendered_chart_svg": chart_svg,
    }

    return render(request, 'github.html', context)

def view_panels(request):
    dboard_panels = DashboardPanel.objects.all()
    context = {
    "all_panels": dboard_panels,
    }
    return render(request, "home_panels.html", context)

def open_csv(): 
    discogs = open("discogs/discogs.csv")
    album_list = []

    for row in csv.DictReader(discogs):
        integer = int(row['Released'])
        album_list.append({
        "Artist": row['Artist'],
        "Title": row['Title'],
        "Label": row['Label'], 
        "Format": row['Format'],
        "Released": integer,
        })

    return album_list   
           

def all_albums(request):
    album_list = open_csv()
    
    chart = pygal.Pie()
    for albums in album_list:
        value = (5)
        label = album_list[0]
        chart.add(label, value)

    chart_svg = chart.render()
    context = {
        "rendered_chart_svg": chart_svg,
    }
  
    return render(request,"all_albums.html", context)



# dashboard ideas: by release year, by artist -- idk how to do that, 
from django.shortcuts import HttpResponse 
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd 
import requests
import csv

def github_api(request):
    response = requests.get('https://api.github.com/users/camibrennan/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

def open_csv(): 
    discogs = open("discogs/discogs.csv")
    for row in csv.DictReader(discogs):
        return("Album Info:", row['Artist'],",", row['Title'], ",",row['Label'], ",", row['Format'],)

def all_albums(request):
    discogs_list = open_csv()
    context = {
    "content": discogs_list,
    }
    return render(request,"all_albums.html", context)


    # def all_albums(request):
    # response = pd.read_csv("discogs/discogs.csv")
    # context = {
    # "content": response,
    # }
    # return render(request,"all_albums.html", context)

#    print(discogs_list.values)
#     print(discogs_list.values[0])

    # Questions: 
    # how to go through a .csv file in a table:
        # for every row in discogs_list show artist , title, label ... do I want to put them in a dictionary?!
    # when do you use models.py/ objects - is that only for user based data?
    # can you import a .csv into SQL? would that be easier? 
    # why do you need to have an app in a django framework?
    # need help understanding context -- is this just for templating?


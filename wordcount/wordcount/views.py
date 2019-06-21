
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def count(request):
    data  = request.GET['fulltextarea']
    word_list = data.split()
    word_len = len(word_list)

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1


    return render(request, 'count.html',{'text': data,'word_len':word_len, 'worddictionary': worddictionary.items()})

def about (request):
    return render(request,'about.html')
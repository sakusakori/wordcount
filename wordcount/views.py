import operator

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello')
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict={}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sortedWords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'text':fulltext, 'count':len(wordlist), 'worddict':sortedWords})

def about(request):
    return render(request, 'about.html')

def saku(request):
    return HttpResponse('Hey saku here!!')
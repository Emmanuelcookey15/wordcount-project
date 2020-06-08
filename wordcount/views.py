from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def aboutpage(request):
    return render(request, 'about.html')

def count(request):
    fullText = request.GET['fulltext']
    print(fullText)
    wordList = fullText.split()

    wordCountDictionary = {}

    for word in wordList:
        if word in wordCountDictionary:
            wordCountDictionary[word] += 1
        else:
            wordCountDictionary[word] = 1

    sortedWords = sorted(wordCountDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fullText, 'count': len(wordList), 'wordsCount': sortedWords})

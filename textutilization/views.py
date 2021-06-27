from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    upper = request.POST.get('upper', 'off')
    capital = request.POST.get('capital', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    print(djtext)

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''

        for char in djtext:
            if char not in punctuations:
                analyzed+=char

        params = {'purpose' : 'Removed Punctuations',
            'analyzed_text' : analyzed}
        djtext = analyzed
    
    if(upper == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose' : 'Changed to Uppercase',
            'analyzed_text' : analyzed}
        djtext = analyzed
    
    if(capital == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed+=char
            analyzed=analyzed
            analyzed=analyzed.capitalize()
        params = {'purpose' : 'Changed to Capitalize',
            'analyzed_text' : analyzed}
        djtext = analyzed

    if(lineremover=='on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed+=char
        params = {'purpose' : 'Removed new lines',
            'analyzed_text' : analyzed}
        djtext = analyzed

    if(spaceremover=='on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1]==' '):
                analyzed+=char
        params = {'purpose' : 'Extra Space Removed',
            'analyzed_text' : analyzed}
        djtext = analyzed


    if(charcount=='on'):
        counter = 0
        analyzed = ''
        for i in djtext:
            counter +=1
        analyzed=str(counter)
        params = {'purpose' : 'Total number of character',
            'analyzed_text' : analyzed}
    if(removepunc!='on' and upper!='on' and capital!='on' and lineremover!='on' and spaceremover!='on' and charcount!='on'):
        return HttpResponse('Error')
    
    return render (request, 'analyze.html', params)

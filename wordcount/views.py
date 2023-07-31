from django.http import HttpResponse
from django.shortcuts import render
import operator #used in count view
def home(request):
    return HttpResponse("Hello this is django 1st page...")
def eggs(request):
    return HttpResponse('<h1>Eggs are great!</h1>')
def potato(request):
    return render(request,'potato.html',{'key':'pair'})
def tomato(request):
    return render(request,'tomato.html')
def count(request):
    fulltext=request.GET['fulltext']
    print(fulltext)#we can see the output in command prompt
    x=fulltext.strip()
    c=x.split(' ')
    print(c)
    wcd=dict()#wordcountdictionary
    for i in c:
        if i not in wcd:
            wcd[i]=1
        else:
            wcd[i]+=1
    swcd=sorted(wcd.items(),key=operator.itemgetter(1),reverse=True)#import operator
    return render(request,'count.html',{'c':len(c),'fulltext':fulltext,'wordcountdict':wcd,'wcd1':wcd.items(),'swcd':swcd})
def about(request):
    return render(request,'about.html')
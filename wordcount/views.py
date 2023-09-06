from django.http import HttpResponse
from django.shortcuts import render
import operator #used in count view
def tomato(request):
    return HttpResponse("Hello this is django 1st page...")
def eggs(request):
    return HttpResponse('<h1>Eggs are great!</h1>')
def potato(request):
    return render(request,'potato.html',{'key':'pair'})
def wordcount(request):
    return render(request,'wordcount.html')
def count(request):
    fulltext=request.GET['fulltext']
    #print(fulltext)#we can see the output in command prompt
    x=fulltext.strip()
    l=[".\r\n",",",'.','?\r\n','?','!\r\n','!']
    for i in l:
        x=x.replace(i," ")
    print(x)
    x=x.strip()
    d=x.split(' ')
    #print(d)
    c=[]
    for i in d:
        c.extend(i.split('\r\n'))
    print(c)
    d=[i.lower() for i in c]

    wcd=dict()#wordcountdictionary
    for i in d:
        if i not in wcd:
            wcd[i]=1
        else:
            wcd[i]+=1
    swcd=sorted(wcd.items(),key=lambda h:h[0])#import operator i.e key=operator.itemgetter(1)
    print(swcd)
    '''nd=dict()
    for i in range(len(c)):
        nd[swcd[i][0]]=swcd[i][1]
    print(nd)'''
    return render(request,'count.html',{'c':len(c),'fulltext':fulltext,'swcd':swcd})
def about(request):
    return render(request,'about.html')
def feedback(request):
    return render(request,'feedback.html')
def thanks(request):
    return render(request,'thanks.html')
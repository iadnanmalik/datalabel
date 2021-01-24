from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from accounts.models import Account
from .models import WordSemantic,Label
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

def wordsemantic(request):
    words= WordSemantic.objects.all().filter(flag=0)
    labels= Label.objects
    for word in words:
         return render(request, 'WordSemantic/homepage.html',{'object': word,'labels':labels})
    return redirect('nomore')
@csrf_exempt
def words(request):

    sentence = str(request.POST.get('sentence'))
    oid = str(request.POST.get('oid'))
    print(sentence)
    print(oid)
    detail= get_object_or_404(WordSemantic,pk=oid)
    if(detail.sentence!=sentence):
        detail.sentence=sentence
        detail.flag=True

    #print(oid)
    accounts=Account.objects.all()
    print(len(accounts))
    name=accounts[len(accounts)-1].fullName
    finalname=''
    if accounts[len(accounts)-1].gender == 'Male':
        finalname= str(accounts[len(accounts)-1].id) +'M'+name 
    if accounts[len(accounts)-1].gender == 'Female':
        finalname= str(accounts[len(accounts)-1].id) +'F'+name 
    if accounts[len(accounts)-1].gender != 'Female' and accounts[len(accounts)-1].gender != 'Male':
        finalname= str(accounts[len(accounts)-1].id) +'N'+name 
        
    detail.username=finalname

    detail.save()
    return HttpResponse('Redirecting')
def next_sentence(request):
    return redirect('wordsemantic')
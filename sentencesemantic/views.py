from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from .models import SentenceSemantic, Label
from accounts.models import Account
from django.conf import settings
from django.shortcuts import render,get_object_or_404

# Create your views here.
#def sentencesemantic(request):
    
 #   my_objects = SentenceSemantic.objects.all().filter(flag=0)
  #  return render(request,'sentencesemantic/homepage.html',{'object',myobject})
   # return render(request,'sentencesemantic/homepage.html')
def sentencesemantic(request):
    sent=SentenceSemantic.objects
    my_objects = SentenceSemantic.objects.all().filter(flag=0)
    labels= Label.objects
    
    for my_object in my_objects:
        print(my_object.sentence)
        return render(request, 'sentencesemantic/homepage.html',{'object': my_object,'labels':labels})
    return redirect('nomore')
def sentences(request,oid):
    if request.method=='POST':
        detail= get_object_or_404(SentenceSemantic,pk=oid)
        detail.flag=True
        detail.labels= request.POST['labels']
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
        return redirect('sentencesemantic')
 
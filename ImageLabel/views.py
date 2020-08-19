from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from accounts.models import Account
from .models import Label, Image
from sentencesemantic.models import SentenceSemantic
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.files import File
from django.http import HttpResponse

# Create your views here.
def imagelabel(request):
    images= Image.objects.all().filter(flag=0)
    labels= Label.objects
    
    for img in images:
        return render(request,'ImageLabel/homepage.html',{'image':img,'labels':labels})
    return redirect('home')
def next_image(request,oid):
    if request.method=='POST':
        detail= get_object_or_404(Image,pk=oid)
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
        return redirect('imagelabel')
 
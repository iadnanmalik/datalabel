from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from accounts.models import Account
from .models import Audio, AudioSentence
from sentencesemantic.models import SentenceSemantic
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.files import File
from django.http import HttpResponse

def audiorecording(request):
    my_objects = AudioSentence.objects.all().filter(flag=0)
    accounts=Account.objects.all()
    name=accounts[len(accounts)-1].fullName
    finalname=''
    if accounts[len(accounts)-1].gender == 'Male':
        finalname= str(accounts[len(accounts)-1].id) +'M'+name 
    if accounts[len(accounts)-1].gender == 'Female':
        finalname= str(accounts[len(accounts)-1].id) +'F'+name 
    if accounts[len(accounts)-1].gender != 'Female' and accounts[len(accounts)-1].gender != 'Male':
        finalname= str(accounts[len(accounts)-1].id) +'N'+name 
    
    for my_object in my_objects:
        return render(request, 'audiorecord/homepage.html',{'object': my_object,'name':finalname})
    return redirect('home')
@csrf_exempt
def next_audio(request):
    audio_file = request.FILES.get('recorded_audio')
    oid = str(request.POST.get('oid'))
    message= Audio()
    print(oid)
    detail= get_object_or_404(AudioSentence,pk=oid)
    print(detail.sentence)
    message.name=detail.sentence
    detail.flag=True
    detail.save()
    message.voice=File(audio_file)

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
        
    message.save()
    return HttpResponse('Redirecting')
def record_next_sentence(request):
    return redirect('audiorecording')
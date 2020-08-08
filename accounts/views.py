from django.shortcuts import render,redirect
from .models import Account
from sentencesemantic.models import SentenceSemantic,Label
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from sentencesemantic import views
def home(request):   

    return render(request, 'accounts/home.html')

def homeForm(request):
    if request.method=='POST':
        if request.POST['name']  and request.POST['email'] and request.POST['gender'] :
                account=Account()
                account.fullName= request.POST['name']
                account.gender= request.POST['gender']
                account.email= request.POST['email']
                

                account.save()
                account=Account.objects
                
                return redirect('sentencesemantic')

        else:
            return render(request,'accounts/homeForm.html', {'error':'Please Fill all the information'})
            
        return render(request, 'accounts/homeForm.html')
    else:

        return render(request, 'accounts/homeForm.html')

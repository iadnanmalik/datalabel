"""datalabel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views
from sentencesemantic import views
import accounts
from WordSemantic import views
from audiorecord import views
from ImageLabel import views
import ImageLabel
import sentencesemantic
import WordSemantic
import audiorecord
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeForm/', accounts.views.homeForm,name='homeForm'),
    path('',accounts.views.home, name='home'),
    path('sentencesemantic/',sentencesemantic.views.sentencesemantic, name='sentencesemantic'),
    path('sentences/<int:oid>/',sentencesemantic.views.sentences,name='sentences'),
    path('words/',WordSemantic.views.words,name='words'),
    path('next_sentence/',WordSemantic.views.next_sentence,name='next_sentence'),
    path('wordsemantic/',WordSemantic.views.wordsemantic, name='wordsemantic'),
    path('audiorecord/',audiorecord.views.audiorecording, name='audiorecording'),
    path('record_next_sentence/',audiorecord.views.record_next_sentence, name='record_next_sentence'),
    path('imagelabel/',ImageLabel.views.imagelabel,name='imagelabel'),
    path('next_image/<int:oid>/',ImageLabel.views.next_image,name='next_image'),
    
    path('next_audio/',audiorecord.views.next_audio,name='next_audio'),
    path('redirectview', accounts.views.redirectview,name='redirectview')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

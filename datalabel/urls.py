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
import sentencesemantic
import WordSemantic
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeForm/', accounts.views.homeForm,name='homeForm'),
    path('',accounts.views.home, name='home'),
    path('sentencesemantic/',sentencesemantic.views.sentencesemantic, name='sentencesemantic'),
    path('sentences/<int:oid>/',sentencesemantic.views.sentences,name='sentences'),
    path('words/',WordSemantic.views.words,name='words'),
    path('next_sentence/',WordSemantic.views.next_sentence,name='next_sentence'),
    path('wordsemantic/',WordSemantic.views.wordsemantic, name='wordsemantic'),
    path('redirectview', accounts.views.redirectview,name='redirectview')
]

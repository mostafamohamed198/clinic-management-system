from turtle import position
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
import datetime
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.db.utils import OperationalError
from datetime import timedelta
from django.views.decorators.csrf import requires_csrf_token
from .forms import *
from django.conf import settings
from datetime import date
from django.db.models import Q 
from django import template
from django.template.defaultfilters import stringfilter


# Create your views here.
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "ophthclinic/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "ophthclinic/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def index(request):
    print(datetime.datetime.today())
    if request.user.is_authenticated:

 
        if request.method == 'POST':
            
            name = request.POST.get('name')
            yearofbirth = request.POST.get('yearofbirth')
            leftleft = request.POST.get('leftleft')
            leftright = request.POST.get('leftright')
            leftmiddle = request.POST.get('leftmiddle')
            rightleft = request.POST.get('rightleft')
            rightmiddle = request.POST.get('rightmiddle')
            rightright = request.POST.get('rightright')
            leftleftr = request.POST.get('leftleftr')
            leftrightr = request.POST.get('leftrightr')
            leftmiddler = request.POST.get('leftmiddler')
            rightleftr = request.POST.get('rightleftr')
            rightmiddler = request.POST.get('rightmiddler')
            rightrightr = request.POST.get('rightrightr')
            idpdist = request.POST.get('idpdist')
            idpread = request.POST.get('idpread')
            diabetesmellitus = request.POST.get('diabetesmellitus', False)
            deabetesnumber = request.POST.get('deabetesnumber')
            hypertension = request.POST.get('hypertension', False)
            ihd = request.POST.get('ihd', False)
            cvs = request.POST.get('cvs', False)
            asthma = request.POST.get('asthma', False)
            atopy = request.POST.get('atopy', False)
            liver = request.POST.get('liver', False)
            kidney = request.POST.get('kidney',False)
            cataract = request.POST.get('cataract',False)
            glucoma = request.POST.get('glucoma', False)
            glucomasurgery = request.POST.get('glucomasurgery', False)
            refractive = request.POST.get('refractive',False)
            medication = request.POST.get('medication')
            bov = request.POST.get('bov', False)
            diplopia = request.POST.get('diplopia',False)
            headache = request.POST.get('headache', False)
            foreign = request.POST.get('foreign', False)
            epiphoria = request.POST.get('epiphoria', False)
            glare = request.POST.get('glare', False)
            note = request.POST.get('note')
            print(f'before;{diabetesmellitus}')
            
            allbool= (diabetesmellitus, hypertension, ihd,cvs, asthma,atopy, liver, kidney, cataract,glucoma, glucomasurgery,refractive, bov,diplopia,headache,foreign, epiphoria, glare)
            for obj in allbool:
                if obj != False:
                    obj = True
                print(obj)
            
            if diabetesmellitus != False:
                 diabetesmellitus = True
            
            if hypertension != False:
                 hypertension = True

            if ihd != False:
                 ihd = True

            if cvs != False:
                 cvs = True 

            if atopy != False:
                 atopy = True

            if asthma != False:
                 asthma = True

            if liver != False:
                 liver = True

            if kidney != False:
                 kidney = True

            if cataract != False:
                 cataract = True

            if glucoma != False:
                 glucoma = True

            if glucomasurgery != False:
                 glucomasurgery = True

            if refractive != False:
                 refractive = True

            if bov != False:
                 bov = True

            if diplopia != False:
                 diplopia = True

            if headache != False:
                 headache = True

            if foreign != False:
                 foreign = True

            if epiphoria != False:
                 epiphoria = True

            if glare != False:
                 glare = True
            print(f'AFTER;{diabetesmellitus}')
            createdclient = client.objects.create(name=name, yearofbirth=yearofbirth )
            createdclient.save()
            createdprofile = info.objects.create(datesubmitted = datetime.datetime.now(),leftleft=leftleft, leftmiddle=leftmiddle, leftright=leftright, rightleft=rightleft, rightmiddle=rightmiddle, rightright=rightright, leftleftr=leftleftr, leftmiddler=leftmiddler, leftrightr=leftrightr, rightleftr=rightleftr, rightmiddler=rightmiddler, rightrightr=rightrightr,idpdist=idpdist, idpread=idpread, diabetesmellitus=diabetesmellitus, deabetesnumber=deabetesnumber, hypertension=hypertension, ihd=ihd, cvs = cvs, asthma=asthma, atopy=atopy,liver=liver,kidney=kidney,cataract=cataract, glucoma =glucoma, glucomasurgery= glucomasurgery, refractive=refractive, medication=medication,bov=bov,diplopia=diplopia, headache=headache,foreign=foreign,epiphoria=epiphoria, glare=glare, note=note)
            createdprofile.save()
            createdclient.lastprofile = createdprofile
            createdclient.relatedprofiles.add(createdprofile)
            createdclient.save()
            print(request.POST.get('hypertension', False))
            
        return render(request, 'ophthclinic/index.html', {'patientinfo':patientinfo})
    
    else:
        return HttpResponseRedirect(reverse("login"))

def patientinfo (request, id):
     selected = client.objects.get(id=id)
     year = datetime.datetime.today().year
     age = int(year) - int(selected.yearofbirth)
     
    #  diabetesmellitus = models.BooleanField(default=None)
    # deabetesnumber = models.FloatField(blank=True, null=True, default=None)
    # hypertension = models.BooleanField(default=False)
    # ihd = models.BooleanField(default=False)
    # cvs = models.BooleanField(default=False)
    # asthma = models.BooleanField(default=False)
    # atopy = models.BooleanField(default=False)
    # liver = models.BooleanField(default=False)
    # kidney
     return render(request, 'ophthclinic/patientinfo.html',{'patient':selected, 'age':age})

class SearchResultsView(ListView):
    model = client
    template_name = "ophthclinic/search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = client.objects.filter(
            Q(name__icontains=query) | Q(yearofbirth__icontains=query)
        )
        return object_list
    

def editpatient(request,idd):
    patient = client.objects.get(id=idd)
    if request.method == 'POST':
            
            name = request.POST.get('name')
            yearofbirth = request.POST.get('yearofbirth')
            leftleft = request.POST.get('leftleft')
            leftright = request.POST.get('leftright')
            leftmiddle = request.POST.get('leftmiddle')
            rightleft = request.POST.get('rightleft')
            rightmiddle = request.POST.get('rightmiddle')
            rightright = request.POST.get('rightright')
            leftleftr = request.POST.get('leftleftr')
            leftrightr = request.POST.get('leftrightr')
            leftmiddler = request.POST.get('leftmiddler')
            rightleftr = request.POST.get('rightleftr')
            rightmiddler = request.POST.get('rightmiddler')
            rightrightr = request.POST.get('rightrightr')
            idpdist = request.POST.get('idpdist')
            idpread = request.POST.get('idpread')
            diabetesmellitus = request.POST.get('diabetesmellitus', False)
            deabetesnumber = request.POST.get('deabetesnumber')
            hypertension = request.POST.get('hypertension', False)
            ihd = request.POST.get('ihd', False)
            cvs = request.POST.get('cvs', False)
            asthma = request.POST.get('asthma', False)
            atopy = request.POST.get('atopy', False)
            liver = request.POST.get('liver', False)
            kidney = request.POST.get('kidney',False)
            cataract = request.POST.get('cataract',False)
            glucoma = request.POST.get('glucoma', False)
            glucomasurgery = request.POST.get('glucomasurgery', False)
            refractive = request.POST.get('refractive',False)
            medication = request.POST.get('medication')
            bov = request.POST.get('bov', False)
            diplopia = request.POST.get('diplopia',False)
            headache = request.POST.get('headache', False)
            foreign = request.POST.get('foreign', False)
            epiphoria = request.POST.get('epiphoria', False)
            glare = request.POST.get('glare', False)
            note = request.POST.get('note')
            print(f'before;{diabetesmellitus}')
            
          
            
            if diabetesmellitus != False:
                 diabetesmellitus = True
            
            if hypertension != False:
                 hypertension = True

            if ihd != False:
                 ihd = True

            if cvs != False:
                 cvs = True 

            if atopy != False:
                 atopy = True

            if asthma != False:
                 asthma = True

            if liver != False:
                 liver = True

            if kidney != False:
                 kidney = True

            if cataract != False:
                 cataract = True

            if glucoma != False:
                 glucoma = True

            if glucomasurgery != False:
                 glucomasurgery = True

            if refractive != False:
                 refractive = True

            if bov != False:
                 bov = True

            if diplopia != False:
                 diplopia = True

            if headache != False:
                 headache = True

            if foreign != False:
                 foreign = True

            if epiphoria != False:
                 epiphoria = True

            if glare != False:
                 glare = True

            patient.name = name
            patient.yearofbirth = yearofbirth
            createdprofile = info.objects.create(datesubmitted = datetime.datetime.now(),leftleft=leftleft, leftmiddle=leftmiddle, leftright=leftright, rightleft=rightleft, rightmiddle=rightmiddle, rightright=rightright, leftleftr=leftleftr, leftmiddler=leftmiddler, leftrightr=leftrightr, rightleftr=rightleftr, rightmiddler=rightmiddler, rightrightr=rightrightr,idpdist=idpdist, idpread=idpread, diabetesmellitus=diabetesmellitus, deabetesnumber=deabetesnumber, hypertension=hypertension, ihd=ihd, cvs = cvs, asthma=asthma, atopy=atopy,liver=liver,kidney=kidney,cataract=cataract, glucoma =glucoma, glucomasurgery= glucomasurgery, refractive=refractive, medication=medication,bov=bov,diplopia=diplopia, headache=headache,foreign=foreign,epiphoria=epiphoria, glare=glare, note=note)
            createdprofile.save()
            patient.lastprofile = createdprofile
            patient.relatedprofiles.add(createdprofile)
            # patient.datesubmitted = datetime.datetime.today()
            # patient.leftleft = leftleft
            # patient.leftmiddle = leftmiddle
            # patient.leftright = leftright
            # patient.rightleft = rightleft
            # patient.rightmiddle = rightmiddle
            # patient.rightright = rightright
            # patient.leftleftr = leftleftr
            # patient.leftmiddler = leftmiddler
            # patient.leftrightr = leftrightr
            # patient.rightleftr = rightleftr
            # patient.rightmiddler = rightmiddler
            # patient.rightrightr = rightrightr
            # patient.diabetesmellitus = diabetesmellitus
            # patient.deabetesnumber = deabetesnumber
            # patient.hypertension = hypertension
            # patient.ihd = ihd
            # patient.cvs = cvs
            # patient.asthma = asthma
            # patient.atopy = atopy
            # patient.liver = liver
            # patient.kidney = kidney
            # patient.cataract = cataract
            # patient.glucoma = glucoma
            # patient.glucomasurgery = glucomasurgery
            # patient.refractive = refractive
            # patient.medication = medication
            # patient.bov = bov
            # patient.diplopia = diplopia
            # patient.headache = headache
            # patient.foreign = foreign
            # patient.epiphoria = epiphoria
            # patient.glare = glare
            # patient.note= note
            patient.save()
            print(f'AFTER;{diabetesmellitus}')
    return render(request, 'ophthclinic/editpatient.html',{'patient':patient})

def related(request, patientid, infoid):
     thepatient = client.objects.get(id=patientid)
     therelated = info.objects.get(id=infoid)
     year = datetime.datetime.today().year
     age = int(year) - int(thepatient.yearofbirth)
     return render(request,'ophthclinic/relatedinfo.html', {'patient':thepatient, 'profile':therelated, 'age':age})

def newdrug(request):
     form = Druginfo()
     if request.method == 'POST':
        print('post')
        form = Druginfo(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
     return render(request, 'ophthclinic/newdrug.html',{'form': form})
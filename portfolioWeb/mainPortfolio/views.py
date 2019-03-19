from django.http import HttpResponse
from mainPortfolio.models import *
from django.template import loader

class indexData():
    def __init__(self):
        try:
            self.header = header.objects.latest('id')
            self.aboutMe = aboutMe.objects.latest('id')
            self.skills = skills.objects.order_by('id')
            self.facts = facts.objects.order_by('id')
        except:
            self.header = self.aboutMe = self.skills = self.facts = []
    
class aboutData():
    def __init__(self):
        try:
            self.aboutMe = aboutMe.objects.latest('id')
            self.expertises = expertises.objects.order_by('id')
            self.qualifications = qualifications.objects.order_by('id').reverse()
        except:
            self.aboutMe = self.expertises = self.qualifications = []



def index(request):
    data = indexData()
    template = loader.get_template('index.html')
    context = {
        'head':data.header,
        'aboutMe':data.aboutMe,
        'skills':data.skills,
        'facts':data.facts,
    }
    return HttpResponse(template.render(context,request))

def about(request):
    template = loader.get_template('about.html')
    data = aboutData()
    #custom code goes here
    context = {
        'aboutMe':data.aboutMe,
        'expertises':data.expertises,
        'qualifications':data.qualifications,
    }
    return HttpResponse(template.render(context,request))

def mywork(request):
    template = loader.get_template('mywork.html')
    projectsList = projects.objects.order_by('id')
    context = {
        'projects':projectsList,
    }
    return HttpResponse(template.render(context,request))


from django.http import HttpResponse
from mainPortfolio.models import *
from django.template import loader
#added dummy comment
class indexData():
    def __init__(self):
        try:
            self.header = header.objects.latest('id')
        except:
            self.header = False
        try:
            self.aboutMe = aboutMe.objects.latest('id')
        except:
            self.aboutMe = False
        try:
            self.skills = skills.objects.order_by('id')
        except:
            self.skills = False
        try:
            self.facts = facts.objects.order_by('id')
        except:
            self.facts = False
        
class getsocialLinks():
    def __init__(self):
        try:
            self.data = socialLinks.objects.latest('id')
            self.valid = True
            self.facebook = self.data.facebook
            self.linkedin = self.data.linkedin
            self.github = self.data.github
            
        except:
            self.valid = False

    
class aboutData():
    def __init__(self):
        try:
            self.aboutMe = aboutMe.objects.latest('id')
        except:
            self.aboutMe = False
        try:
            self.expertises = expertises.objects.order_by('id')
        except:
            self.expertises = False
        try:
            self.qualifications = qualifications.objects.order_by('order').reverse()
        except:
            self.qualifications = False




def index(request):
    data = indexData()
    template = loader.get_template('index.html')
    socialData = getsocialLinks()
    context = {
        'head':data.header,
        'aboutMe':data.aboutMe,
        'skills':data.skills,
        'facts':data.facts,
        'social':socialData,
    }
    return HttpResponse(template.render(context,request))

def about(request):
    template = loader.get_template('about.html')
    data = aboutData()
    socialData = getsocialLinks()
    context = {
        'aboutMe':data.aboutMe,
        'expertises':data.expertises,
        'qualifications':data.qualifications,
        'social':socialData,
    }
    return HttpResponse(template.render(context,request))

def mywork(request):
    template = loader.get_template('mywork.html')
    projectsList = projects.objects.order_by('order')
    socialData = getsocialLinks()
    context = {
        'projects':projectsList,
        'social':socialData,
    }
    return HttpResponse(template.render(context,request))


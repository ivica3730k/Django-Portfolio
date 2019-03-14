from django.http import HttpResponse
from mainPortfolio.models import *
from django.template import loader

class indexData():
    header = header.objects.latest('id')
    aboutMe = aboutMe.objects.latest('id')
    skills = skills.objects.order_by('id')
    facts = facts.objects.order_by('id')
    

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


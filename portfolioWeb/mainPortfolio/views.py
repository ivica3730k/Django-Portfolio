from django.http import HttpResponse
from mainPortfolio.models import *
from django.template import loader

class indexData():
    def __init__(self):
        self.header = header.objects.latest('id')
        self.aboutMe = aboutMe.objects.latest('id')
        self.skills = skills.objects.order_by('id')
        self.facts = facts.objects.order_by('id')
    


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


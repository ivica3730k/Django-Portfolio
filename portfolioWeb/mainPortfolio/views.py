from django.http import HttpResponse
from mainPortfolio.models import post as _post
from mainPortfolio.models import *
from django.template import loader


class static():
    assets = staticAssets.objects.latest('id')
    navi = naviBars.objects.order_by('id')

def index(request):
    template = loader.get_template('index.html')
    sitedata = siteDetails.objects.latest('id')
    article_list = _post.objects.order_by('id')[:5]
    
    staticData=static()
    context = {
        'headline': sitedata.headline,
        'description': sitedata.slogan,
        'background': sitedata.homepicture,
        'article_list':article_list,
        'staticAssets': staticData.assets,
        'navi':staticData.navi,
    }
    return HttpResponse(template.render(context,request))

def postEntry(request,post_id):
    template = loader.get_template('post.html')
    data = _post.objects.get(pk=post_id)
    context = {
        'title':data.title,
        'content':data.content,
        'image':data.featured_image,
        'category':data.category,
        'datePublished':data.publish_date,
    }
    return HttpResponse(template.render(context,request))


from django.contrib.auth.models import User
from rest_framework import viewsets
from sqlinjectionRiskAssessment.serializers import UserSerializer
from .forms import URLForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
import json
from sqlinjectionRiskAssessment.find_sitemap import find_sitemap
from sqlinjectionRiskAssessment.readingJson import read
from subprocess import call
from sqlinjectionRiskAssessment.checkingTools.main import scan
class UserViewSet(viewsets.ModelViewSet):    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

@csrf_exempt
def getUrl(request):
    if request.method == 'POST':
        loadURL = json.loads(request.body.decode('utf-8'))
        weburl = loadURL['url']
        find_sitemap(weburl)
        listURL = read('trafficCapture.json',weburl)
        for i in listURL:
            print(scan(i))

    else:
        return HttpResponse(500)
    return HttpResponse(200)  

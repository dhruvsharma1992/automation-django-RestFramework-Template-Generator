from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import *
from rest_framework.views import APIView
from rest_framework.response import Response  
from rest_framework import authentication, permissions
from  models import *
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import *

from django.forms.models import model_to_dict
import json
from settings import  *



class  test(APIView):
    def get(self, request, *ar, **kwargs):
        list_to_render = ['id: '+str(x) for x in range(0,15)]
        dict_to_render = {}
        for x in range(0,15):
            dict_to_render['key-'+str(x)] =  ' value: '+str(x)
        '''rendering  to a  template'''            
        return render_to_response(os.path.join(TEMPLATE_DIR,'index.html'),{'list':list_to_render,'dict':dict_to_render})

        '''returning a  json-response'''
        #return HttpResponse(json.dumps({'list':list_to_render,'dict':dict_to_render}),content_type='application/json')

        '''returning a  200OK'''
        #return Response()


class get(APIView):
    def get(self, request, *ar, **kwargs):
        get_parameter = request.GET.get('parameter',None)
        return HttpResponse(json.dumps(get_parameter),content_type='application/json')

class post(APIView):
    def post(self, request, *ar, **kwargs):
        return HttpResponse(json.dumps(request.body),content_type='application/json')




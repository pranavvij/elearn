from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse
import json
from lib.core import *

def feedback(request):
    if request.method == 'POST':
        res =  respond('200')
        return HttpResponse(json.dumps(res),content_type="application/json")
    res = respond('405')
    return HttpResponse(json.dumps(res),content_type="application/json")
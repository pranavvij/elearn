from django.shortcuts import HttpResponse
from lib.core import *
from authentication.models import *
from learn.views import *
from deadline.views import *
import uuid,arrow,json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def auth(request):
    res = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        imei_number = data['imei_number']
        try:
            client = create_client(imei_number)
            res = respond('200')
            res['data'] = {
                'access_token': client.access_token,
                'vocabs': get_vocabs(),
                'deadline': get_deadline()
            } 
        except Exception as e:
            print e.message
            res = respond('402')
    else:
        res = respond('405')
    return HttpResponse(json.dumps(res), content_type="application/json")


def create_client(imei_number):
    try:        
        return Client.objects.get(imei_number = imei_number)
    except:    
        client = Client()
        client.refid = uuid.uuid1().hex
        client.access_token = uuid.uuid1().hex
        client.created = arrow.now().timestamp
        client.updated = arrow.now().timestamp
        client.imei_number = imei_number
        client.save()
        return client
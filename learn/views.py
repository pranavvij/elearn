from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from learn.models import *
import json

def index(request):
    if request.method == "GET":
        try:
            vocabs = Vocab.objects.all().order_by('word')
            data = []
            for vocab in vocabs:
                vocab = vocab.__dict__
                vocab.pop('id')
                vocab.pop('_state')
                examples = vocab['examples']
                synonyms = vocab['synonyms']
                vocab.pop('synonyms')
                vocab.pop('examples')
                if 'examples' in examples:
                    vocab['examples'] = examples['examples']
                if 'synonyms' in synonyms:
                    vocab['synonyms'] = synonyms['synonyms']
                if 'partOfSpeech' in synonyms:
                    vocab['partOfSpeech'] = synonyms['partOfSpeech']
                data.append(vocab)
            res = {'data' : data}   
            return HttpResponse(json.dumps(res), content_type = "application/json") 
        except Exception as e:
            return HttpResponse(json.dumps({"message":"Something went wrong"}),content_type = "application/json")
    else:
        return HttpResponse(json.dumps({"message":"Wrong request"}),content_type = "application/json")
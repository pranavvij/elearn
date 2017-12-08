import requests ,json, uuid
from learn.models import *

def execute(words=[]):
    URL = "https://wordsapiv1.p.mashape.com/words/"
    params = {}
    params['X-Mashape-Key'] = 'FSSwKd3umhmshufGKHbvv3ezRozEp1mJrrnjsnmXcXx0Y5or7f'
    recycled = 0
    updated = 0
    for word in words:
        word = word.strip()
        if not Vocab.objects.filter(word = word).exists():
            r = requests.get(url = URL + word,headers=params)
            data = json.loads(r.text)
            vocab = Vocab()
            vocab.word = word
            if 'results' in data:
                for result in data['results']:
                    if 'definition' in result:
                        vocab.definition = result['definition']
                    if 'partOfSpeech' in result:
                        vocab.synonyms['partOfSpeech'] = result['partOfSpeech']
                    if 'synonyms' in result:
                        vocab.synonyms['synonyms'] = result['synonyms']
                    if 'frequency' in data:
                        vocab.frequency = data['frequency']
                    if 'similarTo' in result:
                        vocab.synonyms['similarTo'] = result['similarTo']
                    if 'examples' in result:
                        vocab.examples['examples'] = result['examples']
                    vocab.refid = uuid.uuid1().hex
                    vocab.save()
                    updated = updated + 1
                print "Done .......",word
        else:
            recycled = recycled + 1
            print 'already done',word
    print recycled,updated

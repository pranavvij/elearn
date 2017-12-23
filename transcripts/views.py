from __future__ import unicode_literals
from django.shortcuts import render
from transcripts.models import *


def get_transcripts():
    ts = Transcript.objects.all()
    transcript_dict = []
    for t in ts:
        transcript_dict.append({
            'refid': t.refid,
            'url': t.url,
            'college': t.college,
            'type': t.type
        })
    return transcript_dict
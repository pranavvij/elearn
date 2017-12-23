from __future__ import unicode_literals
from django.shortcuts import render
from deadline.models import *

def get_deadline():
    subjects = Subjects.objects.all().order_by('college__college_name','subject_name')
    subject_dict = []
    for subject in subjects:
        subject_dict.append({
            'refid': subject.refid,
            'college': subject.college.college_name,
            'subject': subject.subject_name,
            'deadline': subject.subject_deadline,
            'type': subject.deadline_type
        })
    return subject_dict
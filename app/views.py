from django.shortcuts import render
import csv
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def export(request):
    profiles=csvs.objects.all()
    response=HttpResponse('text/csv')
    response['Content-Disposition']='attachment; filename=population.csv'
    writer=csv.writer(response)
    writer.writerow(['state','year','men','women','men_child','women_child'])
    profile_fields=profiles.values_list('state','year','men','women','men_child','women_child')
    for i in profile_fields:
        writer.writerow(i)
    return response


def input_user(request):
    form=csv_form()
    d={'form':form}
    if request.method=='POST':
        data=csv_form(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("inserted successfully")
    return render(request, 'input_user.html',d)
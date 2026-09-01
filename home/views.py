from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *

def homepage(request):
    return render(request, "home/home.html")


def doctor(request):

    if request.method == "POST":
        fname = request.POST.get('name')

        Doctor.objects.create(first_name=fname)

        return redirect('/doctor/')

    doctor_list = Doctor.objects.all()

    context = {
        'doctors': doctor_list
    }

    return render(request, 'home/doctor.html', context)



def patient(request):
    if request.method == "POST":
        fname = request.POST.get('name')
    
        Patient.objects.create(first_name=fname)
    
        return redirect('/patient/')
    
    patient_list = Patient.objects.all()

    context = {
        'patients': patient_list
    }

    return render(request, 'home/patient.html', context)

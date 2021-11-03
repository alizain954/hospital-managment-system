from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    d = 0;
    p = 0;
    a = 0;
    for i in doctor:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    context = {'a':a, 'p':p, 'd':d}
    return render(request, 'index.html', context)

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    context = {'pat':pat}
    return render(request, 'view_patient.html', context)

def delete_patient(request, id):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.get(id=id)
    pat.delete()
    return redirect('view_patient')

def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        u = request.POST['name']
        c = request.POST['contact']
        g = request.POST['gender']
        ad = request.POST['address']
        try:
            Patient.objects.create(name=u, mobile=c, gender=g, address=ad)
            error = "no"
        except:
            error = "yes"
    context = {'error':error}
    return render(request, 'add_patient.html', context)

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    context = {'doc':doc}
    return render(request, 'view_doctor.html', context)

def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        u = request.POST['name']
        c = request.POST['contact']
        s = request.POST['special']
        try:
            Doctor.objects.create(name=u, mobile=c, special=s)
            error = "no"
        except:
            error = "yes"
    context = {'error':error}
    return render(request, 'add_doctor.html', context)

def delete_doctor(request, id):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.get(id=id)
    doc.delete()
    return redirect('view_doctor')

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    context = {'appoint':appoint}
    return render(request, 'view_appointment.html', context)

def delete_appointment(request, id):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('view_appointment')

def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t1 = request.POST[ 'time' ]
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t1)
            error = "no"
        except:
            error = "yes"
    context = {'error':error, 'doctor':doctor1, 'patient':patient1}
    return render(request, 'add_appointment.html', context)

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    context = {'error':error}
    return render(request, 'login.html', context)

def logout_admin(request):
    logout(request)
    return redirect('login')

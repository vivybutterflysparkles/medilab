from django.shortcuts import render, redirect
from medilabapp.models import company
from medilabapp.models import Patient,Appointment,Member

# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
                                 member = Member.objects.get(username=request.POST['username'],
                                                             password=request.POST['password']
                                                             )
                                 return render(request,'index.html',{'member':member})

        else:
             return render(request,'login.html')
    else:
        return render(request,'login.html')

def start(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def department(request):
    return render(request,'department.html')

def doctors(request):
    return render(request,'doctors.html')

def patient(request):
    if request.method == 'POST':
        patients = Patient(fullname=request.POST['fullname'],
                           email=request.POST['email'],
                           medicalhistory=request.POST['medicalhistory'],
                           age=request.POST['age'])

        patients.save()
        return redirect('/patient')

    else:
        return render(request,'patient.html')

def contact(request):
    if request.method == 'POST':
        contacts = company(name=request.POST['name'],
                           email=request.POST['email'],
                           message=request.POST['message'],
                           phone=request.POST['phone'],
                           staff=request.POST['staff'])

        contacts.save()
        return redirect('/contact')

    else:
        return render(request,'contact.html')

def appointment(request):
    if request.method == 'POST':
        appointments = Appointment(name=request.POST['name'],
                                   email=request.POST['email'],
                                   phone=request.POST['phone'],
                                   date=request.POST['date'],
                                   department=request.POST['department'],
                                   doctor=request.POST['doctor'],
                                   message=request.POST['message'])
        appointments.save()
        return redirect('/appointment')

    else:
        return render(request,'appointment.html')

def show(request):
    data = Appointment.objects.all()
    return render(request, 'show.html',{'appointment':data})

def delete(request,id):
    myappointment = Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/show')

def register(request):
    if request.method == 'POST':
        members = Member(name=request.POST['name'],
                         username=request.POST['username'],
                         password=request.POST['password'],
                         )
        members.save()
        return redirect('/login')

    else:
        return render(request,'register.html')

def login(request):
    return render (request,'login.html')


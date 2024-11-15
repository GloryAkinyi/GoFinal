from django.shortcuts import render, redirect, get_object_or_404

from myapp.forms import AppointmentForm
from myapp.models import Appointment

# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def doctors(request):
    return render(request,'doctors.html')

def myservice(request):
    return render(request,'services.html')

def appointment(request):
    if request.method == 'POST':
        myappointments=Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            datetime = request.POST['date'],
            department = request.POST['department'],
            doctor= request.POST['doctor'],
            message = request.POST['message']
        )
        myappointments.save()
        return redirect('/appointment')

    else:
        return render(request,'appointment.html')

def show(request):
    allappointments=Appointment.objects.all()
    return render(request,'show.html',{'appointment':allappointments})

def delete(request,id):
    appoint = Appointment.objects.get(id = id)
    appoint.delete()
    return redirect('/show')

def edit(request, id):
    item = get_object_or_404(Appointment, id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = AppointmentForm(instance=item)
    return render(request, 'edit.html', {'form': form})
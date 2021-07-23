from django.forms import models
from django.shortcuts import render, HttpResponseRedirect
from .models import Student
from .forms import StudentRegistration

# This function is used to display and save data into db table
def index(request):
    # Retriving Data from DB table
    students = Student.objects.all() 
    if request.method == "POST":
        model_form = StudentRegistration(request.POST)
        if model_form.is_valid():
            nm = model_form.cleaned_data['name']
            em = model_form.cleaned_data['email']
            ps = model_form.cleaned_data['password']
            reg = Student(name = nm, email = em, password = ps)
            reg.save()
            # After saving value in db, we clear input form fields
            model_form = StudentRegistration()
    else:
        model_form = StudentRegistration()
    return render(request, 'enroll/index.html', {'stdRegForm': model_form, 'students' : students})

# This function is used to edit record from database
def edit_record(request,id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id) # edit data when GET request
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/edit.html', {'editForm': fm})


# This function is used to delete records from database
def delete_record(request, id):
    if request.method == 'POST':
        del_std = Student.objects.get(pk=id)
        del_std.delete()
        return HttpResponseRedirect('/')
        
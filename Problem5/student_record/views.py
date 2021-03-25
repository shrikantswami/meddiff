from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Records
# Create your views here.


def student_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = StudentForm()
        else:
            student = Records.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "student_record/student_form.html", {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Records.objects.get(pk=id)
            form = StudentForm(request.POST, student)
        if form.is_valid():
            form.save()
        return redirect("/student_records/")


def student_list(request):
    context = {'student_list': Records.objects.all()}
    return render(request, "student_record/student_list.html", context)


def student_search(request):
    if request.method == 'GET' and request.GET.get('search'):
        context = {'student_list': [Records.objects.get(pk=request.GET.get('search'))]}
    else:
        context = {'student_list': Records.objects.all()}
    return render(request, "student_record/student_list.html", context)


def student_delete(request, id):
    student = Records.objects.get(pk=id)
    student.delete()
    return redirect('/student_records/')

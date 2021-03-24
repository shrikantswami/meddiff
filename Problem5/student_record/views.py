from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Records
# Create your views here.


def student_form(request):
    if request.method == 'GET':
        form = StudentForm()
        return render(request, "student_record/student_form.html", {'form': form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/student_records/")


def student_list(request):
    context = {'student_list': Records.objects.all()}
    return render(request, "student_record/student_list.html", context)


def student_update(request):
    return


def student_search(request):
    return


def student_delete(request):
    return

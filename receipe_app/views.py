from django.shortcuts import render
from .forms import UserRegistration, ReceipeForm
from . models import User, Receipe
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    form = UserRegistration()
    student = User.objects.all()
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'enroll/index.html', context)

def add(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            stu = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            if (stu == ''):
                user = User(name=name, email=email, password=password)
                
            else:
                user = User(id =stu, name=name, email=email, password=password)
            user.save()
            stuid = User.objects.values()
            # print(stud)  
            student_data = list(stuid)
            return JsonResponse({'status': 'Save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 0})


        
def delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id, "IDDELTE")
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def edit(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id, "IDDELTE")
        student = User.objects.get(pk=id)
        student_data = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'password': student.password
        }
        return JsonResponse(student_data)
    

def home(request):
    form = ReceipeForm()
    student = Receipe.objects.all()
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'receipe.html', context)



def add_vegetable(request):
    if request.method == "POST":
    
        stu = request.POST.get('stuid')
        name = request.POST['fname']
        des = request.POST['des']
        file = request.FILES.get('file')
        # print(file, "IMAGES")

        fss = FileSystemStorage()
        filename = fss.save(file.name, file)
        url = fss.url(filename)
        # print(file.name)

        if (stu == ''):
            user = Receipe(name=name, description=des, image=file)
            
        else:
            user = Receipe(id=stu, name=name, description=des, image=file)

        user.save()
        stuid = Receipe.objects.values()
        # print(stud)  
        student_data = list(stuid)
        return JsonResponse({'status': 'Save', 'student_data': student_data})


def vege_delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')

        pi = Receipe.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})
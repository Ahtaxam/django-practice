from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse,JsonResponse,Http404
from .models import Person,Student
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm,UserRegistration,SignupForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import json

def index(request):
    my_dict={"insert_me":"Text to be inserted"}
    return render(request, "index.html", context=my_dict)


@csrf_exempt
def get_persons(request):
    if request.method == "POST":
        files = request.FILES.get("picture")

        data = request.POST
        data_dict = {key: value[0] for key, value in data.lists()}

        try:
            person = Person.objects.create(**data_dict,picture=files)
            return JsonResponse({"id": person.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": "An error occurred: " + str(e)}, status=500)  
    elif request.method == "GET":
        persons = Person.objects.all()
   
        data = []
        for person in persons:
            data.append({
                "id": person.id,
                "name": person.name,
                "address": person.address,
                "gender": person.gender,
                "age": person.age,
                "dob": person.dob.isoformat(),  
                "email": person.email,
                "picture": person.picture.url if person.picture else None  
            })
        return JsonResponse(data, safe=False)




@csrf_exempt
def update_person(request, id):
    data = request.POST
    data_dict = {key: value[0] for key, value in data.lists()}
    picture = request.FILES.get("picture")
    try:
        person = Person.objects.get(id=id)
        updated_person = Person.objects.filter(id=id).update(**data_dict, picture=picture)
        print(updated_person)
        return HttpResponse(person)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)








def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})



def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return render(request, 'student_not_found.html', {'error_message': 'Student not found.'})
    return render(request, 'student_detail.html', {'student': student})

def student_delete(request, pk):
    print("I am going to delete")
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')






def user_registration(request):
    user = UserRegistration(auto_id=True)
    # user.order_fields(field_order=["name", "email"])

    if request.method == "POST":
        user = UserRegistration(request.POST)
        
        if user.is_valid():
            print(user.cleaned_data)


    return render(request, "user_registration.html", {"form":user})


#  Django authentication

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')  
    else:
        form = SignupForm()
    
    return render(request, 'accounts/register.html', {'form': form})



def user_login(request):
    if request.method == "POST":
        print("HERE", request.POST)
        fm = AuthenticationForm(request=request,data=request.POST)
        print(fm.errors, "FM")
        if fm.is_valid():
            print("ISVALID")
            name = fm.cleaned_data['username']
            passwd = fm.cleaned_data['password']
            user = authenticate(username=name, password=passwd)
            if user is not None:
                print(user, "User")
                print(request.user.is_superuser, "isSUPER")
                login(request, user)
                return HttpResponseRedirect("/")
        else:
            print("INVALID")
    else:
        fm = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': fm})    



#                                                               Start Class Base view


from django.views import View
from django.views.generic import TemplateView, RedirectView

class MyView(View):
    def dispatch(self, request, *args, **kwargs):
        print("Request received and dispatching...")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        print(request, "request")
        print(args, "args")
        print(kwargs, "kwargs")
        return HttpResponse("I am get REquest in View")
    



class DynamicTemplateView(TemplateView):
    name=""
    def get_template_names(self):
        print(self.name, "NAME__")
        if 2 > 1:
            return ['default.html']
        else:
            return ['default_template.html']
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Template View"
        print(context, "CONTEXT")
        return context




class MyRedirectView(RedirectView):
    # pattern_name = 'index'
    url = '/'










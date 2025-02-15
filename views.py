from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm

# Create your views here.
def index(request):
    people= Person.objects.all()
    return render(request, 'index.html', {'people': people})


def  add_person(request):
    if request.method =="POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        
    else:
        form= PersonForm()

    return render(request,"user_form.html" , {"form":form } )

def about(request):
    return render(request,"about.html")




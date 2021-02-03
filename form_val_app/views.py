from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = RegisterForm(request.POST)
        userForm = LogIn(request.POST)
        print(form.is_valid())
        print(form.errors)
        # check whether it's valid
        if form.is_valid():
            # redirect to a new URL
            request.session['first_name'] = request.POST['first_name'] 
            return redirect('/thanks')
        elif userForm.is_valid():
            request.session['email'] = request.POST['email'] 
            return redirect('/login')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
        userForm = LogIn()
        context = { 
            "regForm": form,
            "userForm": userForm
        }
    return render(request, "index.html", context)


def thanks(request):
    return render(request, 'thanks.html')

def login(request):
    userEmail = request.session['email']
    user = User.objects.get(email=userEmail)
    context = {
        "user": user
    }
    return render(request, 'userProfile.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')
from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
from .models import Post
from django.contrib import auth


def home(request):
    return render(request, 'home.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new:list')
    return render(request, 'new/create.html', {'create': create})
    
def log(request):
    posts = Post.objects.all()
    return render(request, 'new/log.html',{'posts':posts})
    
def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'new/show.html', {'show': show})
    
def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                new
                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')


def find_people(request):
    return render(request, 'find_people.html')
    

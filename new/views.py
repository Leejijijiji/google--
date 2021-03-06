from django.shortcuts import render,redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
# from .models import Post
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
            return redirect('new:home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

    
def create(request): 
     
    if request.method == "POST":
        
        print(request.POST)
        title = request.POST.get('title')  
        content = request.POST.get('content')
        writer = request.POST.get('writer')
        post = Post(title=title, content=content, writer=writer)
        post.save()
        return redirect('new:log')
    return render(request, 'new/create.html')

    
    
    
    
def log(request):
    posts = Post.objects.all()
    return render(request, 'new/log.html', {"all_posts" : posts})
    

    
def show(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'new/show.html', {"post" : post })
    
    
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
               

                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')
    return render(request, 'home.html')

def findpeople(request):
    try:
        type_search = request.POST['selSearchType']
        txt_search = request.POST['txtSearch']
        if type_search == "나라":
            people = Post.objects.filter(country=txt_search )
        elif type_search == "지역":
            people = Post.objects.filter(region=txt_search )
        else :
            people = Post.objects.filter(age=txt_search )
        
        
    except:
        people = Post.objects.all()
    return render(request, 'new/findpeople.html', {'people' : people})
    
        
def update(request, id):
    post =  get_object_or_404(Post, pk=id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        writer = request.POST.get('writer')
        post.title = title
        post.content =  content
        post.writer = writer
        post.save()
        return redirect('new:show', post.pk)
    return render(request, 'new/update.html', {"post": post})
    
    
def delete(request, id):
    post =  get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.delete()
        return redirect('new:log')
        

def save(request):
    new_post=Post()
    new_post.name=request.POST['nam']
    new_post.country=request.POST['country']
    new_post.region=request.POST['region']
    new_post.age=request.POST['age']
    new_post.phone=request.POST['phone']
    new_post.introduction=request.POST['introduction']
    new_post.save()
    return render(request,'home.html')

def mypage(request):
    return render(request,'new/mypage.html')
    
    
def introduce(request):
    return render(request, 'introduce.html')
    
def logout(request):
    auth.logout(request)
    return render(request,'login.html')

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from music.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
 
    music = Musics.objects.all()[:7]
    music_list = list(Musics.objects.all().values())[:7]
 
    # data={}
    # if request.method == "GET":
    #     st=request.GET.get('songname')  

    #     if st!=None:
            
    #         music = Musics.objects.filter(Q(title__icontains=st) | Q(artist__icontains=st))
    #         music_list = list(Musics.objects.filter(Q(title__icontains=st) | Q(artist__icontains=st)).values())

    data = {
              'musics': music,
              'music_list': music_list
               }
    
    return render(request, 'index.html',data)


@login_required(login_url='login')
def add(request):

    if(request.method == "POST"):

        title = request.POST.get('title')
        artist = request.POST.get('artist')
        audio = request.FILES.get('audio_file')
        image = request.FILES.get('cover_image')

        data = Musics.objects.create(title=title, artist=artist, audio_file=audio,cover_image=image,user_id=request.user.id)
        data.save()
        return redirect('home')
    
    return render(request,'add.html')


def delete(request,id):

    tep = Musics.objects.get(id=id)
    tep.delete()

    return HttpResponseRedirect('/')


@login_required(login_url='login')
def home(request):

    music = Musics.objects.filter(user_id=request.user.id)[:11]
    music_list = list(Musics.objects.filter(user_id=request.user.id).values())[:11]
 
    data={}
    if request.method == "POST":

        st=request.POST.get('songname')  

        if st!=None:
            
            music = Musics.objects.filter(user_id=request.user.id).filter(Q(title__icontains=st) | Q(artist__icontains=st))
            music_list = list(Musics.objects.filter(user_id=request.user.id).filter(Q(title__icontains=st) | Q(artist__icontains=st)).values())

    data = {
              'musics': music,
              'music_list': music_list
               }


    return render(request,"home.html",data)



def Signup(request):

    if request.method == "POST":

        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if(pass1 != pass2):

            messages.error(request,"Your password and confirm password are not same!")

        else: 

            myuser = User.objects.create_user(uname,email,pass1)
            myuser.save()
            messages.success(request,"Register Successfully")
            return redirect('login')
    
    return render (request,'signup.html')


def Login(request):

    if request.method == "POST":

        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')

        user = authenticate(request,username=uname,password=pass1)

        if user is not None:

            login(request,user)

            return redirect('home')
        else: 
            messages.error(request,"Username or Password is incorrect !!")


    return render(request,'login.html')


def logoutpage(request):

    logout(request)

    return redirect('index')
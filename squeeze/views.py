from squeeze import models
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import redirect, get_object_or_404,Http404
from django.db.models import F
from django.http import HttpResponse,JsonResponse
import uuid
from rest_framework.generics import RetrieveAPIView,ListAPIView,CreateAPIView
from django import forms
from .models import Link
from django.contrib.auth.decorators import login_required
from .serializers import LinkSerializer

def home(request):
	short_url = None
	f=forms.URLField()
	if request.method == "POST":
		custom = request.POST.get("Custom")
		custom = custom.lower()
		if custom:			
			if Link.objects.filter(short_url = custom).exists():
				raise Http404('Url already exists. Please try with another custom URL')
			else:			
				link_db = models.Link()
				link_db.link = request.POST.get("url")
				link_db.link = f.clean(link_db.link)
				link_db.short_url = custom
				short_url = custom
				link_db.save()
		else:			
			link_db = models.Link()
			link_db.link = request.POST.get("url")
			temp = f.clean(link_db.link)
			if Link.objects.filter(link=temp).exists():
				short_url = Link.objects.filter(link=temp)
				return render(request,"index.html",{"short_url":short_url[0].short_url})
				
			link_db.link = temp
			short_url = uuid.uuid4().hex[:6]
			short_url = short_url.lower()
			while(Link.objects.filter(short_url = short_url).exists()):
				short_url = uuid.uuid4().hex[:6]
				short_url = short_url.lower()
			link_db.short_url = short_url
			link_db.save()
	return render(request,"index.html",{"short_url":short_url})
"""
def home(request):
	return render(request,'index.html',{})

def login_view(request):
	if request.method == 'POST':
	    username = request.POST.get('username', None)
	    password = request.POST.get('password', None)
	    if username and password:
	        user = authenticate(username=username, password=password)
	        if user:
	        	if user.is_active:
	        		login(request, user)
	        	redirect('/profile/')
	        else:
	        	return render(request,'login.html',{'err':'Incorrect Username/Password!!'})
	    else:
	    	return render(request,'login.html',{'err':'Enter Username/Password correctly!!'})
	elif request.method == 'GET':
		if request.user.is_authenticated :
			if request.user.is_superuser :
				return redirect('/home/')
			return redirect('/profile/')
		return render(request,'login.html',{})
	return redirect('/profile/')


@login_required
def register(request):
	if not request.user.is_authenticated:
		return redirect('/profile/')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		email = request.POST.get('email', None)
		user, created = User.objects.get_or_create(username=username, email=email)
		if created:
		    user.set_password(password) 
		    user.save()
		    #user.profile.batch = batch
		    user.profile.save()
		    return render(request,'addMember.html',{'msg':"success"})
		else :
			return render(request,'addMember.html',{'err':"User already Exist!!"})
	else:
		return render(request,'addMember.html',{})
"""
def link(request, ids):
	ids=ids.lower()
    try:
        url = Link.objects.get(short_url = ids)
    except Link.DoesNotExist:
    	raise Http404("URL Does Not Exist.")
    else:
        url.hits += 1
        url.save()
        return redirect(url.link)


"""
class LinkList(CreateAPIView):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer
class LinkList(generics.ListCreateAPIView):"""

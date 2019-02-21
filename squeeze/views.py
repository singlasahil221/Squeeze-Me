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
	err_message = None
	f=forms.URLField()
	if request.method == "POST":
		custom = request.POST.get("Custom")
		custom = str(custom).lower()
		if custom:			
			if Link.objects.filter(short_url = custom).exists():
				err_message = 'Url already exists. Please try with another custom URL'
			else:			
				link_db = Link()
				link_db.link = request.POST.get("url")
				link_db.link = f.clean(link_db.link)
				link_db.short_url = custom
				short_url = custom
				link_db.save()
		else:			
			link_db = Link()
			link_db.link = request.POST.get("url")
			temp = f.clean(link_db.link)
			if Link.objects.filter(link=temp).exists():
				short_url = Link.objects.filter(link=temp)
				return render(request,"index.html",{"short_url":short_url[0].short_url})
				
			link_db.link = temp
			short_url = uuid.uuid4().hex[:6]
			short_url = str(short_url).lower()
			while(Link.objects.filter(short_url = short_url).exists()):
				short_url = uuid.uuid4().hex[:6]
				short_url = str(short_url).lower()
			link_db.short_url = short_url
			link_db.save()
	return render(request,"index.html",{"short_url":short_url,"err_message":err_message})

def link(request, ids):
	ids=str(ids).lower()
	try:
		url = Link.objects.get(short_url = ids)
	except Link.DoesNotExist:
		return render(request,"index.html",{"short_url":None,"err_message":"URL Does Not Exist."})
	else:
		url.hits += 1
		url.save()
		return redirect(url.link)


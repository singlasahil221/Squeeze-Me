from squeeze import models
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import redirect, get_object_or_404,Http404
import uuid
from .models import Link

def home(request):
	short_url = None
	f=forms.URLField()
	if request.method == "POST":
		custom = request.POST.get("Custom")
		custom = str(custom).lower()
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
			short_url = str(short_url).lower()
			while(Link.objects.filter(short_url = short_url).exists()):
				short_url = uuid.uuid4().hex[:6]
				short_url = str(short_url).lower()
			link_db.short_url = short_url
			link_db.save()
	return render(request,"index.html",{"short_url":short_url})

def link(request, ids):
	ids=str(ids).lower()
	try:
		url = Link.objects.get(short_url = ids)
	except Link.DoesNotExist:
		raise Http404("URL Does Not Exist.")
	else:
		url.hits += 1
		url.save()
		return redirect(url.link)


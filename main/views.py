from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .models import TutorialCategory, Tutorial, TutorialSeries

def single_slug(request, single_slug):
	categories = [c.category_slug for c in TutorialCategory.objects.all()]
	print(f"Here's matching categories! {categories}")
	if single_slug in categories:
		matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
		series_urls={}
		for m in matching_series.all():
			print(f"Heres matching series !{matching_series}")
			part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series)
			series_urls[m] = part_one

		return render(request, 'main/category.html', {"part_one": series_urls})

	tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
	if single_slug in tutorials:
		return HttpResponse(f"{single_slug} is a category!")

	
	return HttpResponse(f"{single_slug}does not correspond to anything")


def homepage(request):
	return render(request=request,
			template_name= "main/home_contents.html",
			context={}
			)

def register(request):
	

	if request.method == "POST":
		form = MyUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created {username}")
			login(request, user)
			messages.info(request, f"You have been logged in, {username}")
			return redirect("main:homepage")

		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = MyUserForm()

	return render(request,
				  "main/register.html",
				  context={"form":form})

def logout_req(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def overview(request):
	return render( request, "main/overview.html")
def overview_contact(request):
	return render( request, "main/contact.html")

def overview_about(request):
	return render( request, "main/about.html")

def resources(request):
	return render( request, "main/resource.html")	


def api(request):
	return render( request, "main/api.html")	

def overview_aboutcorona(request):
	return render( request, "main/about-corona.html")
	

def survey(request):
	return render( request, "main/survey.html")		

def blogs(request):
	return render( request, "main/blogs.html")	

def aboutus(request):
	return render(request, 'main/aboutus.html')	



def login_req(request):
	
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You have been logged in, {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")


	form = AuthenticationForm()
	return render(request, 'main/login.html', {"form":form})


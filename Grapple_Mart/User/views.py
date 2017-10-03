# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
# Create your views here.

def Login(request):
	context = {}
	# context["NBar"] = "Home"
	if request.GET.get("Log_In"):
		print("Logging in")

	if request.GET.get("Sign_Up"):
		print("Signing Up")
		_Name = request.GET["Full_Name"]
		_Username = request.GET["Username"]
		_Password = request.GET["Password"]
		New_User = User.objects.create_user(_Username, password=_Password)
		New_User.save()
		if request.GET["Type"] == "Athlete":
			New_Athlete = Athlete(User=New_User)
			New_Athlete.Name = _Name
			New_Athlete.save()
		elif request.GET["Type"] == "Instructor":
			New_Instructor = Athlete(User=New_User)
			New_Instructor.Name = _Name
			New_Instructor.save()

	return render(request, "login.html", context)

def Create_Product(request):
	context = {}
	context["NBar"] = "Create_Product"
	return render(request, "create_product.html", context)

def Home(request):
	context = {}
	context["NBar"] = "Home"
	return render(request, "homepage_test.html", context)

def Home_Social(request):
	context = {}
	context["NBar"] = "Social"
	return render(request, "social.html", context)

def Home_Products(request):
	context = {}
	context["NBar"] = "Products"
	return render(request, "purchased_products.html", context)

def Home_Courses(request):
	context = {}
	context["NBar"] = "Courses"
	return render(request, "courses.html", context)
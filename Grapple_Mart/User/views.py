# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files import File
from django.shortcuts import render
from models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import os
# Create your views here.

def Login(request):
	context = {}
	# context["NBar"] = "Home"
	if request.GET.get("Log_In"):
		print("Logging in")
	
	for A in Athlete.objects.all():
		print(A.User.username)

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
	# this will be implemented with django class based views
	for N in Product.objects.all():
		URL = N.File.url[1:]
		print(URL)
		# N.delete()
		# if os.path.isfile(URL):
		# 	print("File Found")
		# 	os.remove(URL)
		# 	 print("Removed Product File")
	context = {}
	context["NBar"] = "Create_Product"
	if request.POST.get("Add_Product"):
		_File = request.FILES['File_Upload']
		Type = request.POST['Product_Type']
		Title = request.POST['Product_Title']
		Description = request.POST['Product_Description']
		Price = float(request.POST['Price'])
		Django_File = File(_File)
		print("File: " + Django_File.name)
		print("Type: " + Type)
		print("Title: " + Title)
		print("Description: " + Description)
		print("Price: " + str(Price))
		New_Product = Product(File=Django_File, Title=Title, Price=Price, Type=Type)
		New_Product.save()
		print("Adding Product")
		return HttpResponseRedirect("/home")
	return render(request, "create_product.html", context)

def Instructor_Profile(request):
	context = {}
	return render(request, "instructor_profile.html", context)


def View_Product(request):
	# this will be implemented with django class based views
	context = {}
	context["NBar"] = "View_Product"
	context["Product_Title"] = "Product Title"
	print(request.session["Product_PK"])
	if "Product_PK" in request.session.keys():
		print("Product PK: " + str(request.session["Product_PK"]))
	Selected_Product = Product.objects.get(pk=int(request.session["Product_PK"]))
	Title = Selected_Product.Title
	Description = Selected_Product.Description
	context["Product_Title"] = Title
	context["Has_Thumbnail"] = Selected_Product.Has_Thumbnail
	if Selected_Product.Has_Thumbnail:
		context["Thumbnail_URL"] = Selected_Product.Thumbnail.url
	context["File_URL"] = Selected_Product.File.url
	context["Type"] = Selected_Product.Type
	context["Product_Description"] = Selected_Product.Description
	context["Price"] = Selected_Product.Price


	if request.method == "POST" and False:
		token = request.POST.get('stripeToken') # Using Flask
		try:

			charge = stripe.Charge.create(
				amount=Selected_Product.Price*100, 
			    currency="usd",
			    description="Purchased Product: " + Selected_Product.Title,
			    source=token,
			    # customer=_ID,
			    )
			request.session["Product_PK"] = Selected_Product.pk
		except stripe.error.CardError as ce:
	        	return False, ce	
		return HttpResponseRedirect("/download-product")

	if request.method == "POST":
		print("POST Detected")
		request.session["Product_PK"] = Selected_Product.pk
		# return HttpResponseRedirect("/test-download")
		return HttpResponseRedirect("/download-product")

	return render(request, "view_product.html", context)

def Download_Product(request):
	context = {}
	context["NBar"] = "Download_Product"

	if "Product_PK" in request.session.keys():
		print("Product PK: " + str(request.session["Product_PK"]))
	Selected_Product = Product.objects.get(pk=int(request.session["Product_PK"]))
	Title = Selected_Product.Title
	File_URL = Selected_Product.File.url

	context["Product_Title"] = Title
	context["File_URL"] = File_URL
	context["Test_Link"] = "/media/Products/Goblet_Box_Squat_Variations_Bissuht.mp4"

	return render(request, "download_product.html", context)

def Test_Download(request):
	context = {}
	if "Product_PK" in request.session.keys():
		print("Product PK: " + str(request.session["Product_PK"]))
		Selected_Product = Product.objects.get(pk=int(request.session["Product_PK"]))
		Title = Selected_Product.Title
		File_URL = Selected_Product.File.url
		context["Test_Link"] = File_URL
		context["File_URL"] = File_URL
	else:
		context["Test_Link"] = "/media/Products/Goblet_Box_Squat_Variations_Bissuht.mp4"

	return render(request, "test_download.html", context)

def Marketplace(request):
	context = {}
	context["NBar"] = "Market"
	context["Test"] = True
	print(context["NBar"])
	context["Product_Title"] = "Product Title"
	Sample_List = [1, 2, 3, 4, 5, 6]

	context["Product_Displays"] = []

	for _Product in Product.objects.all():
		Display_Dict = {}
		Product_Title = _Product.Title
		if _Product.Has_Thumbnail:
			Display_Dict["Thumbnail_URL"] = _Product.Thumbnail.url
		else:			
			Display_Dict["Thumbnail_URL"] = "Placeholders/course_placeholder.jpg"
		Display_Dict["Product_Title"] = Product_Title
		Display_Dict["Product_Description"] = _Product.Description
		Display_Dict["Product_PK"] = _Product.pk
		context["Product_Displays"].append(Display_Dict)

	if request.GET.get("View_Product"):
		print(request.GET["Product_PK"])
		request.session["Product_PK"] = request.GET["Product_PK"]
		return HttpResponseRedirect("/view-product")

	for N in Sample_List:
		Display_Dict = {}
		Product_Title = "Product " + str(N)
		
		Display_Dict["Thumbnail_URL"] = "Placeholders/course_placeholder.jpg"

		Display_Dict["Product_Title"] = Product_Title
		Display_Dict["Product_Description"] = "Place product " + str(N) + " description here."
		# context["Product_Displays"].append(Display_Dict)
	return render(request, "marketplace.html", context)


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
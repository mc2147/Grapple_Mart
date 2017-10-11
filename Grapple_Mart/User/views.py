# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import InstructorEditForm
from django.core.files import File
from django.shortcuts import render
from models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import os
# Create your views here.

Showing_Demo = True

def Generic_Home(request): 
	context = {} 
	context["Test"] = True
	context["Product_Displays"] = []
	context["Show_Login"] = True

	count = 0;
	Num_Min_Products = 5
	for _Product in Product.objects.all():
		Display_Dict = {}
		Product_Title = _Product.Title
		if _Product.Has_Thumbnail:
			Display_Dict["Thumbnail_URL"] = _Product.Thumbnail.url
		else:
			if (count < 1): 			
				Display_Dict["Thumbnail_URL"] = "Placeholders/alloy_strength_warm_up_new.png"
				_Product.Title = "Warm Up: Mobility and Activation Series"
				_Product.save()
				Display_Dict["Long_Title"] = True
				Display_Dict["Product_Title"] = Product_Title
			else: 
				Display_Dict["Thumbnail_URL"] = "Placeholders/course_placeholder.jpg"
				Display_Dict["Product_Title"] = "Sample Product"
		# Display_Dict["Thumbnail_URL"] = "Placeholders/alloy_strength_warm_up.png"
		Display_Dict["Product_Description"] = _Product.Description
		Display_Dict["Product_PK"] = _Product.pk
		Display_Dict["Product_Type"] = _Product.Type
		Display_Dict["Product_Owner"] = _Product.Owner
		Display_Dict["Product_Price"] = _Product.Price
		context["Product_Displays"].append(Display_Dict)

		count += 1

	if request.GET.get("View_Product"):
		print(request.GET["Product_PK"])
		request.session["Product_PK"] = request.GET["Product_PK"]
		return HttpResponseRedirect("/view-product")

	return render(request, "generic_home.html", context)

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

def Instructor_Signup(request):
	context = {}
	return render(request, "instructor_signup.html", context) 


# need to include primary key (pk) to get specific instructors
def Instructor_Profile(request):
	context = {}

	# get instance of instructor based on primary key/id
	# instructor = get_object_or_404(Instructor, pk=pk)

	if request.method == 'POST':
		form = InstructorEditForm(request.POST)

		if form.is_valid(): 

			form_dict = form.cleaned_data

			print form_dict

			# instructor.Bio = form_dict['Bio']
			# instructor.Awards = form_dict['Awards']
			# instructor.Highlights = form_dict['Highlights']

			# instructor.update() # need to add an update function 

	else: 
		form = InstructorEditForm()

	context['form'] = form
		
	return render(request, "instructor_profile2.html", context)


# Need to use primary key (pk) for individual instructors
def Instructor_Profile_Preview(request): 
	context = {}
	if request.GET.get("View_Product"):
		return HttpResponseRedirect("/view-product")
	return render(request, "instructor_profile_user_view.html", context)

def Instructor_Bookings(request): 
	context = {}
	return render(request, "instructor_profile_bookings.html", context)


def View_Product(request):
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
	context["Warm_Up_Thumbnail"] = "Placeholders/alloy_strength_warm_up_new.png"

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
		request.session["Purchased"] = True
		# return HttpResponseRedirect("/test-download")
		return HttpResponseRedirect("/download-product")

	return render(request, "view_product.html", context)

def Download_Product(request):
	context = {}
	context["NBar"] = "Download_Product"
	context["Purchased"] = request.session["Purchased"]
	if "Product_PK" in request.session.keys():
		print("Product PK: " + str(request.session["Product_PK"]))
	Selected_Product = Product.objects.get(pk=int(request.session["Product_PK"]))
	Title = Selected_Product.Title
	File_URL = Selected_Product.File.url
	print(File_URL)

	context["Product_Title"] = Title
	context["File_URL"] = File_URL

	if Showing_Demo:
		context["File_URL"] = "/media/Products/AS_Warm_Up_Series.pdf"
	else:
		context["File_URL"] = "/media/Products/Demo_PDF.pdf"

	if request.method == 'POST':
		print("Form submitted")
		if "Downloaded" in request.POST.keys() and request.POST["Downloaded"] == "Yes":
			print("Downloaded")
			request.session["Purchased"] = False
			return HttpResponseRedirect("/download-product")

	return render(request, "download_product_new.html", context)

# def Download_Product(request):
# 	context = {}
# 	context["NBar"] = "Download_Product"

# 	if "Product_PK" in request.session.keys():
# 		print("Product PK: " + str(request.session["Product_PK"]))
# 	Selected_Product = Product.objects.get(pk=int(request.session["Product_PK"]))
# 	Title = Selected_Product.Title
# 	File_URL = Selected_Product.File.url

# 	context["Product_Title"] = Title
# 	context["File_URL"] = File_URL
# 	context["Test_Link"] = "/media/Products/Goblet_Box_Squat_Variations_Bissuht.mp4"

# 	return render(request, "download_product.html", context)

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

	count = 0;
	for _Product in Product.objects.all():

		Display_Dict = {}
		Product_Title = _Product.Title
		Display_Dict["Product_Price"] = _Product.Price
		if _Product.Has_Thumbnail:
			Display_Dict["Thumbnail_URL"] = _Product.Thumbnail.url
		else:
			if (count < 1): 			
				Display_Dict["Thumbnail_URL"] = "Placeholders/alloy_strength_warm_up_new.png"
				Display_Dict["Product_Title"] = Product_Title
				Display_Dict["Product_Price"] = "12.0"
				_Product.Price = 12.0
				_Product.save()
				Display_Dict["Instructor_Name"] = "Alloy Strength"
			else: 
				Display_Dict["Thumbnail_URL"] = "Placeholders/course_placeholder.jpg"
				Display_Dict["Product_Title"] = "Sample Product"
		Display_Dict["Product_Description"] = _Product.Description
		Display_Dict["Product_PK"] = _Product.pk
		Display_Dict["Product_Type"] = _Product.Type
		Display_Dict["Product_Owner"] = _Product.Owner
		context["Product_Displays"].append(Display_Dict)

		count += 1

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

	
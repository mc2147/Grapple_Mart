from django.core.files import File
from django.shortcuts import render
from User.models import Instructor, Product, Course, Course_Item
from django.http import HttpResponseRedirect
from User.forms import Instructor_Bio_Form


def instructor_home(request):
    context = dict()
    context["NBar"] = "Home"
    _User = request.user

    _Instructor = Instructor.objects.get(User=_User)

    for _Course in _Instructor.Courses.all():
        if not _Course.Confirmed:
            _Course.delete()
    for _Course in Course.objects.all():
        print(_Course.Title)

    if "Tab" not in request.session.keys():
        request.session["Tab"] = "Notifications"

    if request.GET.get("Create_Course_Next"):
        print("Create Course Next")
        print(request.GET["Course_Title"])
        print(request.GET["Course_Description"])
        print(request.GET["Course_Topic"])
        Title = request.GET["Course_Title"]
        Description = request.GET["Course_Description"]
        Topic = request.GET["Course_Topic"]
        New_Course = Course(Owner=_Instructor, Title=Title, Description=Description, Topic=Topic)
        New_Course.save()
        request.session["Course_PK"] = New_Course.pk
        request.session["Tab"] = "Create_Course"
        return HttpResponseRedirect("/create-course")

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
        New_Product = Product(Owner=_Instructor, File=Django_File, Title=Title, Price=Price, Type=Type)
        New_Product.save()
        print("Adding Product")
        # request.session["Session_Message"] = "Product Added!"
        return HttpResponseRedirect("/view-instructor-products")
        # return HttpResponseRedirect("/instructor-home")

    if request.GET.get("Add_Product_Next"):
        request.session["Tab"] = "Add_Product"

    if request.GET.get("Next_Notifications"):
        request.session["Tab"] = "Notifications"

    context["Tab"] = request.session["Tab"]
    # context["Tab"] = "Notifications"
    return render(request, "instructor_home.html", context)


def instructor_view_products(request):
    context = dict()
    context["Products"] = []
    _User = request.user
    _Instructor = Instructor.objects.get(User=_User)
    for _Product in _Instructor.Products.all():
        Display_Dict = {}
        Display_Dict["Type"] = _Product.Type
        Display_Dict["Title"] = _Product.Title
        Display_Dict["Description"] = _Product.Description + "test"
        Display_Dict["Price"] = _Product.Price
        # Display_Dict["Test_URL"] = "/static/Home/video_placeholder.jpg"
        Display_Dict["File_URL"] = _Product.File.url
        # Display_Dict["File_URL"] = _Product.File.url[1:]
        print(_Product.File.url)
        context["Products"].append(Display_Dict)
    return render(request, "instructor_products.html", context)


def create_product(request):
    for N in Product.objects.all():
        URL = N.File.url[1:]
        print(URL)
        # N.delete()
        # if os.path.isfile(URL):
        #     print("File Found")
        #     os.remove(URL)
        #      print("Removed Product File")
    context = dict()
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


def create_course(request):
    context = dict()
    context["Video_Thumbnail"] = "/static/Home/video_placeholder.jpg"

    if "Saved_Order" not in request.session.keys():
        context["Videos"] = [1, 2, 3, 4, 5, 6]
    else:
        context["Videos"] = request.session["Saved_Order"]
    context["Course_Items"] = []
    # print(request.session.keys())
    Course_PK = request.session["Course_PK"]
    _Course = Course.objects.get(pk=Course_PK)

    context["Course_Title"] = _Course.Title
    context["Course_Description"] = _Course.Description
    count = 0
    for N in range(_Course.Items.all().count()):
        count += 1
        _Item = Course_Item.objects.get(Course=_Course, Ordered_ID=count)
    # for _Item in _Course.Items.all():
    #     print(_Item.Ordered_ID)
    #     count += 1
        # if _Item.Ordered_ID == count:
        Display_Dict = {}
        Display_Dict["Title"] = _Item.Title
        Display_Dict["PK"] = _Item.pk
        Display_Dict["File_URL"] = _Item.File.url
        Display_Dict["Ordered_ID"] = _Item.Ordered_ID
        context["Course_Items"].append(Display_Dict)

    if request.POST.get("Add_Item"):
        print("Adding Item")
        Type = request.POST['Item_Type']
        Title = request.POST['Item_Title']
        Description = request.POST['Item_Description']
        print("Type: " + Type)
        print("Title: " + Title)
        print("Description: " + Description)
        print("Adding Product")
        if 'File_Upload' in request.FILES.keys():
            _File = request.FILES['File_Upload']
            Django_File = File(_File)
            print("File: " + Django_File.name)
            Old_Count = _Course.Items.all().count()
            _Course_Item = Course_Item(Course=_Course, File=Django_File, Title=Title, Type=Type,
                                       Description=Description)
            _Course_Item.Ordered_ID = Old_Count + 1
            _Course_Item.save()
            print("New Course Item Added: " + str(_Course_Item.Ordered_ID))
        # if Type == "Video":
        #     Create and assign thumbnail here
        # Ordered_ID = models.IntegerField(default=0)

        # New_Product = Product(File=Django_File, Title=Title, Price=Price, Type=Type)
        # New_Product.save()
        return HttpResponseRedirect("/create-course")
    # Count = 0
    # for Item in _Course.Items.all():
    #     Count += 1
    #     Item_Dict = {}
    #     Item_Dict["Ordered_ID"] = Item.Ordered_ID
    #     Item_Dict["Title"] = Item.Title
    #     if Item.Type == "Video":
        #     Item_Dict["Thumbnail_URL"] = "/static/Home/video_placeholder.jpg"
    #     elif Item.Type == "Video":
        #     Item_Dict["Thumbnail_URL"] = "/static/Home/E_Book_placeholder.jpg"
    #     context["Course_Items"].append(Item_Dict)

    if request.GET.get("Save_Order"):
        print("Creating Course")
        print("Course Items: " + request.GET["Course_Items"])
        Ordered_List = request.GET["Course_Items"].split(",")
        print(Ordered_List)
        request.session["Saved_Order"] = []
        for PK in Ordered_List:
            request.session["Saved_Order"].append(int(PK))
            New_Order = Ordered_List.index(PK) + 1
            _Item = Course_Item.objects.get(Course=_Course, pk=int(PK))
            print(str(Ordered_List.index(PK) + 1) + "th PK: " + PK + _Item.Title)
            _Item.Ordered_ID = New_Order
            _Item.save()
        # print("Creating Course")
        # print(request.GET["Course_Items"])
        # Ordered_Videos = request.GET["Course_Items"].split(",")
        # print(Ordered_Videos)
        # Ordered_List = request.GET["Course_Items"].split(",")
        # for PK in Ordered_List:
            # New_Order = Ordered_List.index(PK) + 1
            # _Item = Course_Item.objects.get(Course = _Course, pk = int(PK))
            # _Item.Ordered_ID = New_Order
            # _Item.save()
        return HttpResponseRedirect("/create-course")
    if request.GET.get("Create_Course"):
        _Course.Confirmed = True
        _Course.save()
        return HttpResponseRedirect("/instructor-home")
    return render(request, "create_course.html", context)


def instructor_courses(request):
    context = dict()
    context["Courses"] = []
    _User = request.user
    _Instructor = Instructor.objects.get(User=_User)
    for _Course in _Instructor.Courses.all():
        Display_Dict = {}
        Display_Dict["Title"] = _Course.Title
        Display_Dict["PK"] = _Course.pk
        context["Courses"].append(Display_Dict)
    if request.GET.get("View_Course"):
        print("Viewing Course")
        request.session["View_Course_PK"] = request.GET["Course_PK"]
        return HttpResponseRedirect("/view-course")
    return render(request, "instructor_courses.html", context)


def view_edit_course(request):
    context = dict()
    context["Video_Thumbnail"] = "/static/Home/video_placeholder.jpg"

    if "Saved_Order" not in request.session.keys():
        context["Videos"] = [1, 2, 3, 4, 5, 6]
    else:
        context["Videos"] = request.session["Saved_Order"]
    context["Course_Items"] = []
    # print(request.session.keys())
    Course_PK = request.session["View_Course_PK"]
    _Course = Course.objects.get(pk=Course_PK)

    context["Course_Title"] = _Course.Title
    context["Course_Description"] = _Course.Description
    context["Course_Price"] = _Course.Price
    count = 0
    for N in range(_Course.Items.all().count()):
        count += 1
        _Item = Course_Item.objects.get(Course=_Course, Ordered_ID=count)
    # for _Item in _Course.Items.all():
    #     print(_Item.Ordered_ID)
    #     count += 1
        # if _Item.Ordered_ID == count:
        Display_Dict = {}
        Display_Dict["Title"] = _Item.Title
        Display_Dict["PK"] = _Item.pk
        Display_Dict["File_URL"] = _Item.File.url
        Display_Dict["Ordered_ID"] = _Item.Ordered_ID
        context["Course_Items"].append(Display_Dict)

    if request.POST.get("Add_Item"):
        print("Adding Item")
        Type = request.POST['Item_Type']
        Title = request.POST['Item_Title']
        Description = request.POST['Item_Description']
        print("Type: " + Type)
        print("Title: " + Title)
        print("Description: " + Description)
        print("Adding Product")
        if 'File_Upload' in request.FILES.keys():
            _File = request.FILES['File_Upload']
            Django_File = File(_File)
            print("File: " + Django_File.name)
            Old_Count = _Course.Items.all().count()
            _Course_Item = Course_Item(Course=_Course, File=Django_File, Title=Title, Type=Type,
                                       Description=Description)
            _Course_Item.Ordered_ID = Old_Count + 1
            _Course_Item.save()
            print("New Course Item Added: " + str(_Course_Item.Ordered_ID))
        # if Type == "Video":
        #     Create and assign thumbnail here
        # Ordered_ID = models.IntegerField(default=0)

        # New_Product = Product(File=Django_File, Title=Title, Price=Price, Type=Type)
        # New_Product.save()
        return HttpResponseRedirect("/view-course")
    # Count = 0
    # for Item in _Course.Items.all():
    #     Count += 1
    #     Item_Dict = {}
    #     Item_Dict["Ordered_ID"] = Item.Ordered_ID
    #     Item_Dict["Title"] = Item.Title
    #     if Item.Type == "Video":
        #     Item_Dict["Thumbnail_URL"] = "/static/Home/video_placeholder.jpg"
    #     elif Item.Type == "Video":
        #     Item_Dict["Thumbnail_URL"] = "/static/Home/E_Book_placeholder.jpg"
    #     context["Course_Items"].append(Item_Dict)

    if request.GET.get("Save_Order"):
        print("Creating Course")
        print("Course Items: " + request.GET["Course_Items"])
        Ordered_List = request.GET["Course_Items"].split(",")
        print(Ordered_List)
        request.session["Saved_Order"] = []
        for PK in Ordered_List:
            request.session["Saved_Order"].append(int(PK))
            New_Order = Ordered_List.index(PK) + 1
            _Item = Course_Item.objects.get(Course=_Course, pk=int(PK))
            print(str(Ordered_List.index(PK) + 1) + "th PK: " + PK + _Item.Title)
            _Item.Ordered_ID = New_Order
            _Item.save()
        # print("Creating Course")
        # print(request.GET["Course_Items"])
        # Ordered_Videos = request.GET["Course_Items"].split(",")
        # print(Ordered_Videos)
        # Ordered_List = request.GET["Course_Items"].split(",")
        # for PK in Ordered_List:
            # New_Order = Ordered_List.index(PK) + 1
            # _Item = Course_Item.objects.get(Course = _Course, pk = int(PK))
            # _Item.Ordered_ID = New_Order
            # _Item.save()
        return HttpResponseRedirect("/view-course")
    if request.GET.get("Delete_Course"):
        _Course.delete()
        return HttpResponseRedirect("/instructor-home")
    return render(request, "view_course.html", context)


def instructor_profile(request):
    context = dict()
    Bio_Form = Instructor_Bio_Form()
    context["Bio_Form"] = Bio_Form
    context["NBar"] = "Profile"
    return render(request, "instructor_profile.html", context)

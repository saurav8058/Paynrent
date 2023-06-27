from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from paynrentapp.serializers import SubCategorySerializers
from paynrentapp.models import SubCategory
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def SubCategoryInterface(request):
    return render(request,"SubCategoryInterface.html")
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def SubCategorySubmit(request):
    if request.method == 'POST':
        subcategory_serializers = SubCategorySerializers(data=request.data)
        if subcategory_serializers.is_valid():
            subcategory_serializers.save()
            return render(request,"SubCategoryInterface.html",{'message':"Record Submitted Sucessfully"})
        return render(request,"SubCategoryInterface.html",{'message':"Fail to Submit Record"})
'''
@api_view(['GET','POST',])
def DisplaySubCategory(request):
    try:
        if request.method == 'GET':
            list_subcategory = SubCategory.objects.all()
            list_subcategory_serializers = SubCategorySerializers(list_subcategory,many=True)
            records = tuple_to_dict.ParseDict(list_subcategory_serializers.data)
            return render(request,"SubCategoryDisplay.html",{'data':records})
    except Exception as e:
        print("Error",e)
        return render(request,"SubCategoryDisplay.html",{'data':{}})
'''
@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def DisplaySubCategory(request):
    try:
        if request.method == 'GET':
            q = "select S.*,(select C.categoryname from paynrentapp_category C where C.id=S.category_id) as categoryname from paynrentapp_subcategory S"
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("xxxxxxxxxx",records)
            

            return render(request,"SubCategoryDisplay.html",{'data':records})
    except Exception as e:
        print("Error",e)
        return render(request,"SubCategoryDisplay.html",{'data':{}})


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def DisplaySubCategoryJSON(request):
    try:
        if request.method == 'GET':
            q="select * from paynrentapp_subcategory where category_id={0}".format(request.GET['cid'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            #print("xxxxxxxx",cursor.fetchall())
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            
            return JsonResponse(record,safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse([],safe=False)



@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def DisplaySubCategorybyId(request):
    try:
        if request.method == 'GET':
            q = "select S.*,(select C.categoryname from paynrentapp_category C where C.id=S.category_id) as categoryname from paynrentapp_subcategory S where S.id={0}".format(request.GET['id'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictSingleRecord(cursor)
            print("xxxxxxxx",record)
            return render(request,"SubCategoryDisbyId.html",{'data':record})
    except Exception as e:
        print("Error",e)
        return render(request,"SubCategoryDisbyId.html",{'data':record})
@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def EditSubCategory(request):
    try:
        if request.method == 'GET':
            if request.GET['btn'] == 'Edit':
                subcategory = SubCategory.objects.get(pk=request.GET['id'])
                subcategory.category_id = request.GET['category_id']
                subcategory.company_name = request.GET['company_name']
                subcategory.subcategory_name = request.GET['subcategory_name']
                subcategory.description = request.GET['description']
                subcategory.save()
            else:
                subcategory = SubCategory.objects.get(pk=request.GET['id'])
                subcategory.delete()
            return redirect('/api/displaysubcategory') 
    except Exception as e:
        print("Error :" ,e)
        return redirect('/api/displaysubcategory') 
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def DisplaySubCategoryIcon(request):
    try:
        if request.method == 'GET':
            return render(request,"DisplaySubCategoryIcon.html",{'data':request.GET})
    except Exception as e:
        print("Error : ",e)
        return render(request,"DisplaySubCategoryIcon.html",{'data':[]})       
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def SubCategoryIconSave(request):
    try:
        if request.method == 'POST':
            subcategory = SubCategory.objects.get(pk=request.POST['id'])
            subcategory.icon = request.FILES['icon']
            subcategory.save()
            return redirect('/api/displaysubcategory')
    except Exception as e:
        print("Error : ",e)
        return redirect('/api/displaysubcategory')
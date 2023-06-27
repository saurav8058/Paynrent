from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from rest_framework.decorators import api_view
from paynrentapp.serializers import AdminstratorSerializer
from paynrentapp.models import Administrator
from . import tuple_to_dict

@api_view(['GET','POST','DELETE'])
def AdminLogin(request):
    return render(request,"AdminLogin.html",{'message':''})

@api_view(['GET','POST','DELETE'])
def CheckAdminLogin(request):
    try:
        if request.method == 'GET':
            print("ONE")
            q = "select * from  paynrentapp_administrator  where (mobileno='{0}' or emailid='{0}') and password='{1}'".format(request.GET['mobileno'],request.GET['password'])

            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("Check",record)
            if(len(record)==0):
               
                return render(request,"AdminLogin.html",{'message':"Inavlid Adminid/Password"})
            else:
               
               return render(request,"DashBoard.html",{'data':record[0]})
            
            
    except Exception as e:
        print("Error : ",e)
        return render(request,"DashBoard.html",{'data':[]})
   
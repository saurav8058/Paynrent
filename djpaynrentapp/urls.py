"""djpaynrentapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from paynrentapp import category_view
from paynrentapp import subcategory_view
from paynrentapp import vehicle_view
from paynrentapp import admin_login
from paynrentapp import user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/categoryinterface',category_view.CategoryInterface),
    re_path(r'^api/categorysubmit',category_view.CategorySubmit),
    re_path(r'^api/displaycategory',category_view.DisplayCategory),
    re_path(r'^api/display_category_by_id',category_view.DisplayByCategoryID),
    re_path(r'^api/categoryedit/$',category_view.EditCategory),
    re_path(r'^api/display_category_icon/$',category_view.DisplayCategoryIcon),
    re_path(r'^api/cat_save_icon',category_view.Category_Save_Icon),
    re_path(r'^api/json_displaycategory',category_view.DisplayCategoryJSON),
    re_path(r'^api/subcategoryinterface',subcategory_view.SubCategoryInterface),
    re_path(r'^api/subcategorysubmit/&',subcategory_view.SubCategorySubmit),
    re_path(r'^api/displaysubcategory',subcategory_view.DisplaySubCategory),
    re_path(r'^api/subcategorydisplaybyid',subcategory_view.DisplaySubCategorybyId),
    re_path(r'^api/editsubcategory',subcategory_view.EditSubCategory),
    re_path(r'^api/subcategoryicondisplay',subcategory_view.DisplaySubCategoryIcon),
    re_path(r'^api/savesubcategoryicon',subcategory_view.SubCategoryIconSave),
    re_path(r'^api/jsondisplaysubcategory',subcategory_view.DisplaySubCategoryJSON),

    re_path(r'^api/vehicleinterface',vehicle_view.VehicleInterface),
    re_path(r'^api/vehiclesubmit',vehicle_view.VehicleSubmit),
    re_path(r'^api/vehicledisplay',vehicle_view.VehicleDisplay),
    re_path(r'^api/displayvehiclebyid',vehicle_view.VehicleDisplayById),
    re_path(r'^api/editvehicle',vehicle_view.EditVehicle),
    re_path(r'^api/vehicleicondisplay',vehicle_view.DisplayVehicleIcon),
    re_path(r'^api/savevehicleicon',vehicle_view.SaveVehicleIcon), 
    
    re_path(r'^api/adminlogin',admin_login.AdminLogin), 
    re_path(r'^api/checkadminlogin',admin_login.CheckAdminLogin), 
    re_path(r'^api/index',user_view.Index), 
    re_path(r'^api/displayvehicleforuser',user_view.VehicleDisplayForUser), 
    re_path(r'^api/uservehiclelist',user_view.PageUserVehicleList), 
     re_path(r'^api/displayselectedvehicle',user_view.DisplaySelectedVehicle), 
     re_path(r'^api/showvehiclelist',user_view.ShowVehicleList), 
     re_path(r'^api/setemailmobile',user_view.SetMobileAndEmail), 

    ]

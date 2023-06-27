from rest_framework import serializers 
from paynrentapp.models import Category
from paynrentapp.models import SubCategory
from paynrentapp.models import Vehicle
from paynrentapp.models import Administrator
class CategorySerializer(serializers.ModelSerializer):
 class Meta:
        model = Category
        fields = ('id','categoryname','description','icon')
class SubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id','category_id','company_name','subcategory_name','description','icon')

class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id','category_id','subcategory_id','model_year','variant','price','insured','registration_no','owner_name','mobile_no','color','fuel_type','no_of_seats','transmission_type','icon')        
 

class AdminstratorSerializer(serializers.ModelSerializer):
 class Meta:
        model = Administrator
        fields = ('id','adminname','mobileno','emailid','password')


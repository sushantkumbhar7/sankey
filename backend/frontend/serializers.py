from rest_framework import serializers
from .models import registration,addfurniture
class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields="__all__"

class showSerializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields=('name','email','contact')

class addfurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model=addfurniture
        fields="__all__"

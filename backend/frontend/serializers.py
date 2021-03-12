from rest_framework import serializers
from .models import registration
class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields="__all__"

class showSerializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields=('name','email','contact')

from rest_framework import serializers
from .models import Universitiesm

class UniversitiesmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universitiesm
        fields = '__all__'
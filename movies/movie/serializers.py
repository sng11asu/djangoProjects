from rest_framework import serializers
from .models import Collections, Counter

class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ['title', 'uuid', 'description', 'movies']

class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields= ['status']
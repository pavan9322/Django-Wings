from rest_framework import serializers
from .models import Member

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
from rest_framework import serializers
from .models import User, Company, Job

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # hashes the password
        user.save()
        return user
    


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'created_by']
        
    
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
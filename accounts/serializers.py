from .models import CustomUser
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type":"password"})
    password2 = serializers.CharField(write_only=True, style={"input_type":"password"})

    class Meta:
        model = CustomUser
        fields = ['id','username','password','password2']
        read_only_fields = ['id','username']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Пароли не совпадають!')
        raise attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user
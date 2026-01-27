from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    custom_message = serializers.SerializerMethodField()
    
    class Meta:
        model = Member    # <--- Member라는 클래스 자체를 넣어야 합니다.
        fields = '__all__'       
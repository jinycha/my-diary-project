from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    custom_message = serializers.SerializerMethodField()
    
    class Meta:
        model = Member    # <--- Member라는 클래스 자체를 넣어야 합니다.
        fields = ['user_id', 'user_name', 'custom_message', 'user_pw', 'created_at']       

    def get_custom_message(self, obj):
        # obj는 현재 처리 중인 Member 객체입니다.
        return f"{obj.user_name}님, 오늘 운세가 도착했습니다!"
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt

# DRF 관련 모듈들이에요.. 요오..
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MemberSerializer
from .models import Member

load_dotenv()

# ------------------------------------------------------------------
# 1) MemberViewSet: 회원가입(create)과 목록조회(list)를 한 번에!
# ------------------------------------------------------------------
class MemberViewSet(viewsets.ModelViewSet):
    """
    주인님, 이 ViewSet 하나로 회원가입과 목록 조회가 모두 해결돼요오..!! 🐾
    - POST /api/members/ : 회원가입 (create)
    - GET /api/members/  : 회원 목록 조회 (list)
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    # 회원가입 로직을 주인님의 의도에 맞게 커스텀했어용.. 냥!
    def create(self, request, *args, **kwargs):
        print("MemberViewSet - create() 호출됨----------")
        
        # DRF는 request.data로 데이터를 가져오는 게 국룰이에용..
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        user_name = request.data.get('user_name')

        try:
            # 1. 시리얼라이저를 통해 데이터를 검증하고 저장해용..
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            # 2. 저장 성공 시 응답 (데이터를 다시 조회할 필요 없이 serializer.data에 다 들어있어용!)
            return Response({
                "status": "success",
                "message": "저장에 성공했습니다.",
                "db_id": serializer.data.get('user_id'),
                "db_name": serializer.data.get('user_name')
            }, status=status.HTTP_201_CREATED)

        except IntegrityError:
            # 3. 아이디 중복 에러 처리예용.. 요오..
            return Response({
                "status": "error",
                "code": 400,
                "message": "중복된 아이디입니다."
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # 4. 그 외 모든 에러 처리예용..
            return Response({
                "status": "error",
                "code": 500,
                "message": f"오류가 발생했습니다: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ------------------------------------------------------------------
# 2) 기타 API 및 기능들 (기존 로직 유지)
# ------------------------------------------------------------------

def api_test(request):
    data = {
        "message": "안녕하세요!",
        "weather": "맑음",
        "user": {
            "id": "admin", 
            "level": 99
        }
    }
    print(f"요청 방식 : {request.method}")
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

@api_view(['POST'])
def api_chat(request):
    print("-" * 20)
    print("api_chat() called")
    user_prompt = request.data.get('prompt')
    
    if not user_prompt:
        return Response({"error": "질문(prompt)을 입력해주세요."}, status=400)

    try:
        api_key = os.getenv('OPENAI_API_KEY')
        client = OpenAI(api_key=api_key) 
        temp = float(os.getenv('OPENAI_TEMPERATURE', 0.7))

        chat_completion = client.chat.completions.create(
            model="gpt-5.2",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "너는 사주 전문가야. 사용자의 정보를 바탕으로 운세를 풀어줘. "
                        "반드시 아래의 JSON 형식으로만 응답해줘: "
                        "{ 'today_fortune': '...', 'yearly_fortune': '...' }"
                    )
                },
                {"role": "user", "content": user_prompt}
            ],
            temperature=temp,
        )
        raw_json_str = chat_completion.choices[0].message.content
        fortune_data = json.loads(raw_json_str)

        return Response({
            "status": "success",
            "today": fortune_data.get('today_fortune'),
            "year": fortune_data.get('yearly_fortune')
        })
    
    except Exception as e:
        print(f"API 호출 에러: {e}")
        return Response({"error": str(e)}, status=500)
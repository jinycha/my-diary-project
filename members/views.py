import os # [추가] 환경변수 읽기용
from dotenv import load_dotenv # [추가] .env 파일 로드용
from django.shortcuts import render, redirect
from django.http import JsonResponse
from openai import OpenAI

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MemberSerializer
from .models import Member

load_dotenv()

# Create your views here.
def signup(request):

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')

        m = Member(
            user_id=user_id,
            user_pw=user_pw,
            user_name=user_name
        )
        s=m.save()
        print("=="*50)
        print(f"save result : {s}")
        print("=="*50)

        return redirect('/admin/')
    else:
         return render(request, 'signup.html')
    
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
    print(f"GET데이터 : {request.GET}")
    

    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def api_members(request):
   
   print("api_members-------------")
   members = Member.objects.all()
   serializer = MemberSerializer(members, many=True)
   return Response(serializer.data)

from django.contrib import admin
from django.urls import path
from members import views

import json

@api_view(['POST'])
def api_chat(request):
    print("-"*20)
    print("api_chat() called")
    user_prompt = request.data.get('prompt')
    
    if not user_prompt:
        return Response({"error": "질문(prompt)을 입력해주세요."}, status=400)

    try:
        api_key = os.getenv('OPENAI_API_KEY')
        client = OpenAI(api_key=api_key) 

        # model_name = os.getenv('OPENAI_MODEL', 'gpt-5.2') # 기본값 설정 가능
        # temperature는 숫자로 변환이 필요합니다 (os.getenv는 문자열을 돌려주기 때문)
        temp = float(os.getenv('OPENAI_TEMPERATURE', 0.7))

        
        chat_completion = client.chat.completions.create(

            model="gpt-5.2",
            response_format={"type": "json_object"},
            
        #    
        messages=[
                {
                    "role": "system", 
                    "content": (
                        "너는 사주 전문가야. 사용자의 정보를 바탕으로 운세를 풀어줘. "
                        "반드시 아래의 JSON 형식으로만 응답해줘: "
                        "{ 'today_fortune': '...', 'yearly_fortune': '...' }" # JSON 구조 정의
                    )
                },
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
        )
        raw_json_str = chat_completion.choices[0].message.content
        fortune_data = json.loads(raw_json_str)

        print(f"today : {fortune_data.get('today_fortune')}")
        print(f"year : {fortune_data.get('yearly_fortune')}")

        return Response({
            "status": "success",
            "today": fortune_data.get('today_fortune'),
            "year": fortune_data.get('yearly_fortune')
        })
    
    except Exception as e:
        print(f"API 호출 에러: {e}")
        return Response({"error": str(e)}, status=500)
    # return Response({
    #     "question": user_prompt,
    #     "answer": ai_response
    
    # return Response({
    #     "today_fortune": today.strip(),
    #     "yearly_fortune": yearly.strip()
    # })

    
# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('signup/', views.signup),
# ]


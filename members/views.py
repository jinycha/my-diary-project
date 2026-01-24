
from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MemberSerializer

from .models import Member

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
   
   members = Member.objects.all()
   serializer = MemberSerializer(members, many=True)
   return Response(serializer.data)

from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', views.signup),
]


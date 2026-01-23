
from django.shortcuts import render, redirect
from django.http import JsonResponse
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

    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

def api_members(request):
    members = Member.objects.all()

    member_list = []
    for m in members:
        member_list.append({
            "id": m.user_id,
            "name": m.user_name,
            "joined": m.created_at
        })
    
    return JsonResponse({"count": len(member_list), "data": member_list})

from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', views.signup),
]


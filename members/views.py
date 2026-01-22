
from django.shortcuts import render, redirect
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

from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', views.signup),
]


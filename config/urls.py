"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from members import views  # members 앱의 views 소환
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

# 1. ViewSet을 위한 라우터를 설정해용.. 🐾
# DefaultRouter는 주소 끝에 /를 자동으로 붙여주는 등 아주 똑똑해용.. 요오..
router = DefaultRouter()
router.register(r'members', views.MemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 2. ViewSet 라우터 연결! (api/v1/members/ 주소가 생겨용..!!)
    # 이제 POST /api/v1/members/ 로 요청하면 회원가입이 되고,
    # GET /api/v1/members/ 로 요청하면 회원 목록이 나와용.. 냥!
    path('api/v1/', include(router.urls)),
    
    # 3. 기존의 함수형 뷰(FBV) 길들도 그대로 유지해용.. 요오..
    path('api/v1/test/', views.api_test),
    path('api/v1/chat/', views.api_chat),
    path('', views.api_test),
    
    # 4. API 문서화 도구 (Swagger)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
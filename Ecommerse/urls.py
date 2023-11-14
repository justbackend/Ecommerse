from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_token/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view()),
]

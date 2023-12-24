from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import RegisterAPIView, LoginAPIView

app_name = 'auth'

urlpatterns = [
    path('signup/', RegisterAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
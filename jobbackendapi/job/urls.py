from rest_framework import routers
from .views import UserViewSet, CompanyViewSet, JobViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'job', JobViewSet)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
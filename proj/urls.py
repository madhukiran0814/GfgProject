from django.urls import path
from .views import WorkListAPIView

urlpatterns = [
    path('api/works', WorkListAPIView.as_view(), name='work-list'),
]

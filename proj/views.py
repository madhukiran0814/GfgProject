from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from .models import Work, Artist
from .serializers import WorkSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class WorkListAPIView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artist__name']
    ordering_fields = ['id', 'link', 'work_type']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        artist = self.request.query_params.get('artist', None)
        work_type = self.request.query_params.get('work_type', None)
        if artist is not None:
            queryset = queryset.filter(artist__name=artist)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)
        return queryset


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        password = make_password(self.request.data.get('password'))
        serializer.save(password=password)

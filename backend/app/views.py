from django.shortcuts import render, redirect
from .models import Feedback
from .serializers import FeedbackSerializaer
from rest_framework import viewsets, permissions

def home(request):
    return redirect('/admin/')

class FeedbackViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializaer
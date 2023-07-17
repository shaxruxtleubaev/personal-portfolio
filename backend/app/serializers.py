from rest_framework.serializers import *
from .models import Feedback

class FeedbackSerializaer(ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'
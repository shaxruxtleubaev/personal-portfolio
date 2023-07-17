from django.contrib.admin import *
from .models import Feedback

@register(Feedback)
class FeedbackAdmin(ModelAdmin):

    list_display = ('id', 'name', 'date',)
    list_display_links = ('name',)
    exclude = ('date',)
from django.db.models import *
from django.utils.timezone import now

class Feedback(Model):

    name = CharField('Name', max_length=128)
    email = EmailField('Email')
    subject = CharField('Subject', max_length=128)
    message = TextField('Message')
    date = DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'
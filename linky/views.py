from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView

class Laughs(ListView):
    template_name = ' chat/room.html'
    context_object_name = 'laughs'

    def get_queryset(self):
        return TheManWhoLaugh.objects.all().order_by('published_date')


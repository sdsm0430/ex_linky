# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from linky.models import TheManWhoLaugh

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    prev = 0
    next = 1
    print(request)

    #if request.method == "GET":
    #    prev += 1
    #    next += 1
    #    print(prev)
    #    print(next)
    #else:
    #    pass
    #print(type(prev))
    #print(next)
    laughs = TheManWhoLaugh.objects.order_by('-published_date')[prev:next]
    laughs_next = TheManWhoLaugh.objects.order_by('-published_date')[prev+1:next+1]
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)), 'laughs':laughs, 'laughs_next':laughs_next
    })

# chat/views.py
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from linky.models import *
import json

def main(request):
    reviews = TMWL_review.objects.order_by('-published_date')[:5]
    return render(request, 'chat/main.html', {'reviews':reviews, })

def choice(request):
    return render(request, 'chat/choice.html',{})

def review(request):
    reviews = TMWL_review.objects.all()
    if request.method =="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.published_date = timezone.now()
            review.save()
            return redirect('review')
    else:
        form = ReviewForm()
    return render(request, 'chat/review.html', {'reviews':reviews, 'form':form, })

def index(request):
    if request.method =="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.published_date = timezone.now()
            review.save()
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'chat/index.html', {'form':form,})

def user_korean(request):
    password = TMWL_password.objects.all()
    return render(request, 'chat/user_korean.html', {'password': mark_safe(json.dumps(toJson_password(password))),})

def user_japanese(request):
    password = TMWL_password.objects.all()
    return render(request, 'chat/user_japanese.html', {'password': mark_safe(json.dumps(toJson_password(password))),})

def user_english(request):
    password = TMWL_password.objects.all()
    return render(request, 'chat/user_english.html', {'password': mark_safe(json.dumps(toJson_password(password))),})

def user_chinese(request):
    password = TMWL_password.objects.all()
    return render(request, 'chat/user_chinese.html', {'password': mark_safe(json.dumps(toJson_password(password))),})

@login_required
def room(request, room_name):
    korean = TMWL_korean.objects.order_by('-published_date')
    japanese = TMWL_japanese.objects.order_by('-published_date')
    chinese = TMWL_chinese.objects.order_by('-published_date')
    english = TMWL_english.objects.order_by('-published_date')
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'json_korean': mark_safe(json.dumps(toJson(korean))),
        'json_japanese': mark_safe(json.dumps(toJson(japanese))),
        'json_chinese': mark_safe(json.dumps(toJson(chinese))),
        'json_english': mark_safe(json.dumps(toJson(english))),
    })

def toJson(queryset):
    """
    TODO:
        model의 파라미터를 모두 json형태로 바꾸어야 한다.

        현재는 actor, song, music 만을 보낸다.

    :param
        queryset: django queryset
    :return:
        output: dict
    """
    out = {} # output 변수
    cnt = 0
    for laugh in queryset:
        song = laugh.song
        actor = laugh.actor
        music = laugh.music

        tmp = {'song':song, 'actor':actor,'music':music}
        out[cnt] = tmp
        cnt += 1
    return out

def toJson_password(queryset):
    out = {}
    cnt = 0
    for laugh in queryset:
        password = laugh.password

        tmp = {'password':password,}
        out[cnt] = tmp
        cnt += 1
    return out
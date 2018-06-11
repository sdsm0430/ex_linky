# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from linky.models import *
import json

def operate_list(request):
    musicals = Musical.objects.order_by('-published_date')
    return render(request,'chat/operate_list.html', {'musicals':musicals, })

def main_list(request):
    musicals = Musical.objects.order_by('-published_date')
    return render(request, 'chat/main_list.html', {'musicals': musicals, })

def main_detail(request, pk):
    """
    메인 페이지

    linky.models.py 'Review' 모델 전달 완료
    TODO:
        추가적으로 'Musical' 모델 전달 필요
        pk 전달 필요
    :param
        request
    :return
        reviews queryset
    """
    musical = get_object_or_404(Musical, pk=pk)
    reviews = Review.objects.all().filter(musical=pk)[:5]
    return render(request, 'chat/main.html', {'musical':musical, 'reviews':reviews, })

def choice(request):
    """
    언어 선택 페이지

    :param
        request
    """
    return render(request, 'chat/choice.html',{})

def review(request, pk):
    """
    리뷰 페이지

    리뷰 작성 폼과 리뷰 리스트 전달
    :param
        request
        pk : Musical 함수 연동
    :return:
        ReviewForm(작성폼), queryset(리뷰 리스트)
    """
    musical = get_object_or_404(Musical, pk=pk)
    reviews = Review.objects.all().filter(musical=pk)
    if request.method =="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.musical = musical
            print(review.musical)
            review.published_date = timezone.now()
            review.save()
            return redirect('review', pk=musical.pk)
    else:
        form = ReviewForm()
    return render(request, 'chat/review.html', {'reviews':reviews, 'form':form, 'pk':pk})

def index(request):
    """
    필요 없는 함수
    """
    if request.method =="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review = form.save(commit=False)
            Review.published_date = timezone.now()
            Review.save()
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'chat/index.html', {'form':form,})

def user_korean(request):
    """
    korean 자막 송출 페이지
    TODO:
        pk 값 적용하며 password 전달
        get_object_or_404 활용
    """
    password = Musical.objects.all()
    return render(request, 'chat/user_korean.html', {'password': mark_safe(json.dumps(toJson_password(password))),})

def user_japanese(request):
    """
    japanese 자막 송출 페이지
    """
    password = Musical.objects.all()
    return render(request, 'chat/user_japanese.html', {'password': mark_safe(json.dumps(toJson_password(password))),})

def user_english(request):
    """
    english 자막 송출 페이지
    """
    password = Musical.objects.all()
    return render(request, 'chat/user_english.html', {'password': mark_safe(json.dumps(toJson_password(password))),})

def user_chinese(request):
    """
    chinese 자막 송출 페이지
    """
    password = Musical.objects.all()
    return render(request, 'chat/user_chinese.html', {'password': mark_safe(json.dumps(toJson_password(password))),})

@login_required
def room(request, room_name):
    a = Script.objects.all().filter(language='한국어')
    b = Script.objects.all().filter(language='영어')
    c = Script.objects.all().filter(language='일본어')
    d = Script.objects.all().filter(language='중국어')
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'json_korean': mark_safe(json.dumps(toJson(a))),
        'json_japanese': mark_safe(json.dumps(toJson(b))),
        'json_chinese': mark_safe(json.dumps(toJson(c))),
        'json_english': mark_safe(json.dumps(toJson(d))),
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
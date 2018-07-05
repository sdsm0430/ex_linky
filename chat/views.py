# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from .forms import *
from linky.models import *
import json

@login_required
def operate_list(request):
    musicals = Musical.objects.order_by('-published_date')
    return render(request,'chat/operate_list.html', {
        'musicals':musicals,
    })

@login_required
def password(request, pk):
    musical = get_object_or_404(Musical, pk=pk)
    if request.method == "POST":
        form = PasswordForm(request.POST, instance=musical)
        if form.is_valid():
            password = form.save(commit=False)
            password.save()
            return redirect('operate_list')
            #return redirect('operate_list', pk=musical.pk)
    else:
        form = PasswordForm(instance=musical)
    return render(request, 'chat/password.html', {
        'form': form,
        'musical':musical,
    })

@login_required
def admin_password(request, pk):
    musical = get_object_or_404(Musical, pk=pk)
    if request.method == "POST":
        form = AdminPasswordForm(request.POST, instance=musical)
        if form.is_valid():
            admin_password = form.save(commit=False)
            admin_password.save()
            return redirect('operate_list')
    else:
        form = AdminPasswordForm(instance=musical)
    return render(request, 'chat/admin_password.html', {
        'form': form,
        'musical':musical,
    })

@login_required
def operate(request, room_name):
    musical = get_object_or_404(Musical, title=room_name)
    a = Script.objects.all().filter(language='한국어', musical=musical)
    b = Script.objects.all().filter(language='영어', musical=musical)
    c = Script.objects.all().filter(language='일본어', musical=musical)
    d = Script.objects.all().filter(language='중국어', musical=musical)
    return render(request, 'chat/operate.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'json_korean': mark_safe(json.dumps(toJson(a))),
        'json_japanese': mark_safe(json.dumps(toJson(b))),
        'json_chinese': mark_safe(json.dumps(toJson(c))),
        'json_english': mark_safe(json.dumps(toJson(d))),
    })

def main_list(request):
    musicals = Musical.objects.order_by('-published_date')
    return render(request, 'chat/main_list.html', {
        'musicals': musicals,
    })

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
    return render(request, 'chat/main.html', {
        'musical':musical,
        'reviews':reviews,
        'pk':pk,
    })

def apply(request, pk):
    musical = get_object_or_404(Musical, pk=pk)
    if request.method =="POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            apply = form.save(commit=False)
            apply.musical = musical
            apply.save()
            return redirect('apply_complete', pk=musical.pk)
    else:
        form = ApplyForm()
    return render(request, 'chat/apply.html', {
        'form':form,
        'pk':pk,
    })

def apply_image(request, pk):
    musical = get_object_or_404(Musical, pk=pk)
    if request.method =="POST":
        form = ApplyImageForm(request.POST, request.FILES)
        if form.is_valid():
            apply_image = form.save(commit=False)
            apply_image.musical = musical
            apply_image.save()
            return redirect('apply_image', pk=musical.pk)
    else:
        form = ApplyImageForm()
    return render(request, 'chat/apply_image.html', {
        'form':form,
        'pk':pk,
    })

def apply_complete(request, pk):
    musical = get_object_or_404(Musical, pk=pk)
    return render(request, 'chat/apply_complete.html', {
        'musical':musical,
        'pk':pk,
    })

def choice(request, pk):
    """
    언어 선택 페이지

    :param
        request, pk
    """
    musical = get_object_or_404(Musical, pk=pk)
    return render(request, 'chat/choice.html', {
        'pk':pk,
        'musical':musical,
    })

def user_korean(request, room_name):
    """
    korean 자막 송출 페이지
    TODO:
        pk 값 적용하며 password 전달 (clear)
        get_object_or_404 활용 (no)
    """
    musical = get_object_or_404(Musical, title=room_name)
    password = Musical.objects.all().filter(title=room_name)
    return render(request, 'chat/user_korean.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'password': mark_safe(json.dumps(toJson_password(password))),
        'musical':musical,
    })

def user_japanese(request, room_name, pk):
    """
    japanese 자막 송출 페이지
    """
    musical = get_object_or_404(Musical, pk=pk)
    password = Musical.objects.all()
    return render(request, 'chat/user_japanese.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'musical':musical,
        'password': mark_safe(json.dumps(toJson_password(password))),
        'pk':pk,
    })

def user_english(request, room_name, pk):
    """
    english 자막 송출 페이지
    """
    musical = get_object_or_404(Musical, pk=pk)
    password = Musical.objects.all()
    return render(request, 'chat/user_english.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'password': mark_safe(json.dumps(toJson_password(password))),
        'pk':pk,
        'musical':musical,
    })

def user_chinese(request, room_name, pk):
    """
    chinese 자막 송출 페이지
    """
    musical = get_object_or_404(Musical, pk=pk)
    password = Musical.objects.all()
    return render(request, 'chat/user_chinese.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'password': mark_safe(json.dumps(toJson_password(password))),
        'pk':pk,
        'musical':musical,
    })

def toJson(queryset):
    """
    TODO:
        model의 파라미터를 모두 json형태로 바꾸어야 한다.

        현재는 actor, song, music 만을 보낸다.

    :param
        queryset: django queryset
    :return:
        output: dic
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

def review(request, pk):
    """
    리뷰 페이지

    리뷰 작성 폼과 리뷰 리스트 전달
    :param
        request
        pk : Musical 함수 연동( ? )
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
            review.published_date = timezone.now()
            review.save()
            return redirect('review', pk=musical.pk)
    else:
        form = ReviewForm()
    return render(request, 'chat/review.html',  {
        'reviews':reviews,
        'form':form,
        'pk':pk,
    })
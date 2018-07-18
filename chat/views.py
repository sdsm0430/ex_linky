# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from .forms import *
from linky.models import *
import json

@login_required
def operate_list(request):
    """
    오퍼레이팅 뮤지컬 리스트 페이지

    :param
        request
    :return
        musical queryset
    """
    musicals = Musical.objects.order_by('-published_date')
    return render(request,'chat/operate_list.html', {
        'musicals':musicals,
    })

@login_required
def password(request, pk):
    """
    오페레이팅 패스워드 등록 페이지

    :param
        request, pk
    :return:
        form, musical model
    """
    musical = get_object_or_404(Musical, pk=pk)
    if request.method == "POST":
        form = PasswordForm(request.POST, instance=musical)
        if form.is_valid():
            password = form.save(commit=False)
            password.save()
            return redirect('operate', room_name=musical)
            #return redirect('operate_list', pk=musical.pk)
    else:
        form = PasswordForm(instance=musical)
    return render(request, 'chat/password.html', {
        'form': form,
        'pk': pk,
        'musical':musical,
    })

@login_required
def admin_password(request, pk):
    """
    오퍼레이팅 패스워드 확인 페이지

    TODO:
    유효성 검사

    :param
        request, pk
    :return
        form, musical model
    """
    musical = get_object_or_404(Musical, pk=pk)
    if request.method == "POST":
        form = AdminPasswordForm(request.POST, instance=musical)
        if form.is_valid():
            admin_password2 = form.save(commit=False)
            admin_password2.save()
            if musical.admin_password == musical.admin_password2:
                return redirect('operate_password', pk=musical.pk)
            else:
                return redirect('admin_password', pk=musical.pk)
    else:
        form = AdminPasswordForm(instance=musical)
    return render(request, 'chat/admin_password.html', {
        'form': form,
        'musical':musical,
    })

@login_required
def operate(request, room_name):
    """
    자막 오퍼레이팅 페이지

    :param
        request, room_name
    :return
        room_name(json), script queryset 4종류
    """
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

    :param
        request, pk
    :return
        reviews queryset, pk, musical model
    """
    musical = get_object_or_404(Musical, pk=pk)
    reviews = Review.objects.order_by('-published_date').all().filter(musical=pk)[:5]
    return render(request, 'chat/main.html', {
        'musical':musical,
        'reviews':reviews,
        'pk':pk,
    })

def apply(request, pk):
    """
    자막 요청 페이지

    :param
        request, pk
    :return
        form, pk
    """
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
    """
    이미지 업로드 뷰, 현재 사용하지 않음
    """
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
    """
    자막 요청 완료 페이지

    :param
        request, pk:
    :return
        musical model, pk
    """
    musical = get_object_or_404(Musical, pk=pk)
    apply = Apply.objects.last()
    return render(request, 'chat/apply_complete.html', {
        'musical':musical,
        'apply':apply,
        'pk':pk,
    })


def choice(request, pk):
    """
    언어 선택 페이지

    :param
        request, pk
    :return
        musical model, pk
    """
    musical = get_object_or_404(Musical, pk=pk)
    return render(request, 'chat/choice.html', {
        'pk':pk,
        'musical':musical,
    })

def user_korean(request, room_name):
    """
    korean 자막 송출 페이지

    :param
        request, room_name
    :return
        room_name(json), musical model, musical queryset
    """
    musical = get_object_or_404(Musical, title=room_name)
    password = Musical.objects.all().filter(title=room_name)
    return render(request, 'chat/user_korean.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'password': mark_safe(json.dumps(toJson_password(password))),
        'musical':musical,
    })

def user_japanese(request, room_name):
    """
    japanese 자막 송출 페이지

    """
    musical = get_object_or_404(Musical, title=room_name)
    password = Musical.objects.all().filter(title=room_name)
    return render(request, 'chat/user_japanese.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'musical':musical,
        'password': mark_safe(json.dumps(toJson_password(password))),
    })

def user_english(request, room_name):
    """
    english 자막 송출 페이지

    """
    musical = get_object_or_404(Musical, title=room_name)
    password = Musical.objects.all().filter(title=room_name)
    return render(request, 'chat/user_english.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'password': mark_safe(json.dumps(toJson_password(password))),
        'musical':musical,
    })

def user_chinese(request, room_name):
    """
    chinese 자막 송출 페이지

    """
    musical = get_object_or_404(Musical, title=room_name)
    password = Musical.objects.all().filter(title=room_name)
    return render(request, 'chat/user_chinese.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'password': mark_safe(json.dumps(toJson_password(password))),
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

def review(request, room_name):
    """
    리뷰 페이지
    리뷰 작성 폼과 리뷰 리스트 전달

    :param
        request, room_name
    :return:
        review queryset, form,  pk
    """
    musical = get_object_or_404(Musical, title=room_name)
    print(musical.title)
    reviews = Review.objects.all().filter(musical__title=room_name)
    if request.method =="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.musical = musical
            review.published_date = timezone.now()
            review.save()
            return redirect('main_detail', pk=musical.pk)
    else:
        form = ReviewForm()
    return render(request, 'chat/review.html',  {
        'musical':musical,
        'form':form,
    })

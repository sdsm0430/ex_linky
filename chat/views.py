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
    musical list page for operating

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
def admin_password(request, pk):
    """
    password check page for operating

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
def password(request, pk):
    """
    password enrollment for operating

    :param
        request, pk
    :return:
        pk, form, musical model
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
def operate(request, room_name):
    """
    operating page

    :param
        request, room_name
    :return
        room_name(json), script queryset to json(case 4)
    """
    musical = get_object_or_404(Musical, title=room_name)
    a = Script.objects.all().filter(language='한국어', musical=musical)
    b = Script.objects.all().filter(language='일본어', musical=musical)
    c = Script.objects.all().filter(language='중국어', musical=musical)
    d = Script.objects.all().filter(language='영어', musical=musical)
    return render(request, 'chat/operate.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'json_korean': mark_safe(json.dumps(toJson(a))),
        'json_japanese': mark_safe(json.dumps(toJson(b))),
        'json_chinese': mark_safe(json.dumps(toJson(c))),
        'json_english': mark_safe(json.dumps(toJson(d))),
    })

def main_list(request):
    """
    musical list page for user

    :param
        request
    :return
        musical queryset
    """
    musicals = Musical.objects.order_by('-published_date')
    return render(request, 'chat/main_list.html', {
        'musicals': musicals,
    })

def main_detail(request, pk):
    """
    musical detail page for user

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
    apply page for script request

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

def apply_complete(request, pk):
    """
    apply complete page about script request

    :param
        request, pk:
    :return
        musical model, apply quertset, pk
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
    language choice page

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
    korean script page for user

    :param
        request, room_name
    :return
        room_name(json), musical model, musical queryset for password
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
    japanese script page for user

    """
    musical = get_object_or_404(Musical, title=room_name)
    password = Musical.objects.all().filter(title=room_name)
    return render(request, 'chat/user_japanese.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'password': mark_safe(json.dumps(toJson_password(password))),
        'musical':musical,
    })

def user_english(request, room_name):
    """
    english script page for user

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
    chinese script page for user

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
    queryset to json

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
    """
    queryset to json

    """
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
    review page for user

    :param
        request, room_name
    :return:
        musical model, form
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

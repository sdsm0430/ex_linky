from django.db import models
from django.utils import timezone
import csv, os
from django.conf import settings

#뮤지컬에 대한 정보를 담고 있는 모델
class Musical(models.Model):
    title = models.CharField(null=True, max_length=50)                                                  #뮤지컬
    published_date = models.DateTimeField(blank=True, null=True)                                        #모델 생성 일시
    producer = models.CharField(null=True, max_length=50)                                               #제작사
    producer_logo = models.ImageField(blank=True, null=True)                                            #제작사 로고
    term = models.CharField(null=True, max_length=50)                                                   #공연기간
    place = models.CharField(null=True, max_length=50)                                                  #공연장소
    slogan = models.CharField(null=True, max_length=100)                                                #대표문구
    genre = models.CharField(null=True, max_length=30)                                                  #장르
    viewing_age = models.IntegerField(default=0, blank=True)                                            #관람연령
    runtime = models.IntegerField(default=0, blank=True)                                                #런타임
    language = models.CharField(null=True, max_length=30)                                               #언어
    poster = models.ImageField(blank=True, null=True)                                                   #포스터
    banner_image = models.ImageField(blank=True, null=True)                                             #배너이미지
    background_image = models.ImageField(blank=True, null=True)                                         #배경이미지
    repre_image = models.ImageField(blank=True, null=True)                                              #대표이미지
    csv = models.FileField(blank=True, null=True)                                                       #자막 업로드를 쉽게 하기 위한 csv 필드
    password = models.CharField(null=True, max_length=50)                                               #영상 송출 시 유출 방지를 위한 password 저장 필드

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self):
        """
        csv 저장될 때 계속 Script 업데이트.
        """
        super(Musical,self).save()




#각 뮤지컬 모델에 One to Many로 연결한 리뷰 모델
class Review(models.Model):
    musical = models.ForeignKey(Musical, related_name='reviews')        #OnetoMany 연결
    review = models.CharField(null=True, max_length=200)                #리뷰 필드
    published_date = models.DateTimeField(blank=True, null=True)        #리뷰 작성 일시
    star = models.IntegerField(default=0, blank=True)                   #별점

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.review

#각 뮤지컬 모델에 One to Many로 연결하여 자막 송출을 위한 실질적 정보를 담고 있는 스크립트 모델
class Script(models.Model):
    musical = models.ForeignKey(Musical, related_name='scripts')        #OnetoMany 연결
    language = models.CharField(null=True, max_length=30)               #언어
    music = models.CharField(null=True, max_length=200)                 #음악
    actor = models.CharField(null=True, max_length=50)                  #배우
    song = models.CharField(null=True, max_length=400)                  #노래, 가사
    order = models.IntegerField(null=True)                              #순서

    def __str__(self):
        return self.language

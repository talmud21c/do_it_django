from django.db import models
import os

# Create your models here.

class Post(models.Model):
    # 게시글 제목 정의
    title = models.CharField(max_length=50)
    # 글 내용 정의 (최대 길이 지정 필요 없음)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    # 작성일 정의
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author 추후 작성 예정

    # Django에서 제공하는 기본 함수
    def __str__(self):
        return f'[{self.id}] [{self.title}]'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    # 직접 만든 함수수
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
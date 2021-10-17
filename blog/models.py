from django.db import models

# Create your models here.

class Post(models.Model):
    # 게시글 제목 정의
    title = models.CharField(max_length=50)
    # 글 내용 정의 (최대 길이 지정 필요 없음)
    content = models.TextField()

    # 작성일 정의
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author 추후 작성 예정

    def __str__(self):
        return f'[{self.id}] [{self.title}]'
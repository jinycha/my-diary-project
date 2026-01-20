from django.db import models

class Member(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # 👇 여기에 테이블 이름 설정 추가
    class Meta:
        db_table = 'tb_member'  # 원하는 테이블 이름

    def __str__(self):
        return self.user_name
    
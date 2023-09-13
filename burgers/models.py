from django.db import models

# Create your models here.
# 햄버거를 나타내는 Model 클래스 정의 시작
class Burger(models.Model):
    # 문자열을 저장하는 CharField
    name = models.CharField(max_length=20)
    # 숫자를 저장하는 IntegerField
    price = models.IntegerField(default=0)
    # 숫자를 저장하는 IntegerField
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
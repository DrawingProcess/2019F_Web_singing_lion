from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    user = models.ForeignKey(User, related_name='rooms', on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    NOREBANG = [('1', '수노래방'), ('2', '라이브노래방'), ('3', '딩기딩기노래방'), ('4','씽씽노래방')]
    norebang = models.CharField(max_length=30, choices=NOREBANG)
    GENRES = [('힙합', '힙합'), ('발라드', '발라드'), ('팝송', '팝송'), ('R&B', 'R&B'), ('댄스', '댄스'), ('락', '락')]
    genre = models.CharField(max_length=10, choices=GENRES)
    # genre = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    AGES = [('10대', '10대'), ('20대', '20대'), ('30대', '30대'), ('40대', '40대'), ('50대', '50대')]
    ages = models.CharField(max_length=10, choices=AGES)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
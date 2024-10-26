from django.db import models

class Word(models.Model):
  id = models.AutoField(primary_key=True)
  word = models.CharField(max_length=30, verbose_name='Word')
  mean = models.TextField(max_length=400, verbose_name='意味')
  cnt = models.IntegerField(default=0)
  by_cnt = models.IntegerField(default=10, verbose_name='何回テストで消す？')
  rdmflag = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
  return self.word
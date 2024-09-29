from django.shortcuts import render, redirect, get_object_or_404
from .forms import WordForm
from .models import Word
import random
# from django.http import HttpResponse


def index(request):
  return render(request, 'word/index.html')

def wordWrite(request):
  if request.method == 'POST':
    form = WordForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('word:index')

  form = WordForm()
  return render(request, 'word/word_write.html', {'form':form})

def wordList(request):
  words = Word.objects.all()
  print(words)
  params = {
    'words':words,
  }
  return render(request, 'word/word_list.html', params)

def wordDetail(request, id):
  word = get_object_or_404(Word, id=id)
  params = {
    'word':word,
  }
  return render(request, 'word/word_detail.html', params)

def wordTest(request):
  words = Word.objects.all()
  print('-------wordTest------')
  # print(words[0].__dict__)
  # print(words[0].word)
  # print(words[rnd].id)
  # print(len(words))
  # print(rnd)
  wordsLen = len(words)
  rnd = random.randint(0,wordsLen - 1)
  params = {
    'word':words[rnd],
  }
  return render(request, 'word/word_test.html', params)

def wordResult(request, id):
  word = get_object_or_404(Word, id=id)
  params = {
    'word':word,
  }
  return render(request, 'word/word_result.html', params)
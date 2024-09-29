from django.urls import path

from . import views

app_name = 'word'
urlpatterns = [
    path("", views.index, name="index"),
    path("word_write", views.wordWrite, name="word_write"),
    path("word_list", views.wordList, name="word_list"),
    path("word_detail/<int:id>", views.wordDetail, name="word_detail"),
    path("word_test", views.wordTest, name="word_test"),
    path("word_result/<int:id>", views.wordResult, name="word_result"),
    path("word_delete/<int:id>", views.wordDelete, name="word_delete"),
]
# finance_app/urls.py

from django.urls import path
from .views import answer_question

urlpatterns = [
    path('answer/', answer_question, name='answer-question'),
]

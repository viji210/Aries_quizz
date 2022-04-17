from django.urls import path
from . import views

app_name = "quizbrain"

urlpatterns = [
    path("", views.home, name="home_page"),
    path("quiz/<str:category>", views.quiz, name="quiz"),
]

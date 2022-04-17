from django.urls import path
from . import views

app_name = "quizbrain"

urlpatterns = [
    path("", views.home, name="home_page"),
    path("quiz/<str:category>/<int:q_no>", views.quiz, name="quiz"),
]

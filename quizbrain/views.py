from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . import models

question_index = 0
show_next = False


# Create your views here.
def home(request):
    global question_index
    question_index = 0
    category = models.Quiz.objects.values_list('category', flat=True)
    category_cleaned = list(dict.fromkeys(category))
    print(category_cleaned)
    context = {"category": category_cleaned}
    return render(request, "quizbrain/home.html", context=context)


def quiz(request, category):
    global question_index
    global show_next
    question, end_of_quiz = None, False

    all_category = models.Quiz.objects.values_list('category', flat=True)
    category_cleaned = list(dict.fromkeys(all_category))

    print(category)
    question_list = models.Quiz.objects.filter(category=category).order_by('pk').all()

    total_question = len(question_list)

    if question_index < total_question:
        show_next = False
        question = question_list[question_index]

    elif total_question == question_index:
        question_index = 0
        question = question_list[question_index]
        end_of_quiz = True

    if request.method == "POST":
        print(request.POST)

        if request.POST.get('move_on', False) == "move_on":
            question_index += 1
            return redirect(reverse("quizbrain:quiz", args=[request.POST['question_category']]))

        elif request.POST.get('multichoice') == request.POST['real_answer']:
            # question_index += 1
            show_next = True
            messages.success(request, question.right_feedback)
        elif request.POST.get('multichoice') is None:
            messages.warning(request, "SELECT A FIELD TO PROCEED")
        else:
            messages.warning(request, question.wrong_feedback)

    context = {
        "question": question,
        "question_no": question_index + 1,
        "choice_list": {"choice_a": question.choice_1,
                        "choice_b": question.choice_2,
                        "choice_c": question.choice_3,
                        "choice_d": question.choice_4,
                        "choice_e": question.choice_5,
                        "choice_f": question.choice_6,},
        "end_of_quiz": end_of_quiz,
        "show_next": show_next,
        "category": category_cleaned
    }

    return render(request, "quizbrain/quiz.html", context=context)

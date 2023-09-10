from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import (
    UserResponseModelMultiOption,
    UserResponseModelFreeTextOption,
    UserResponseModelTrueFalseOption,
    UserINFO,
)
from TestingSystem.models import Question, Test, Option, TrueFalse, FreeText
from .forms import RegistrationForm
from django.utils.safestring import mark_safe
from AssignLinks.models import AssignLinkModel
import pytz
from django.utils import timezone
from datetime import datetime


def answer_question_view(request, assign_id, user_id, assign_slug):
    user = get_object_or_404(UserINFO, pk=user_id)
    assign_model = get_object_or_404(
        AssignLinkModel, pk=assign_id, slug_field=assign_slug
    )
    random_questions = assign_model.test_foreign.test_random.all().order_by('order')
    questions = [question.question for question in random_questions]
    uzbekistan_timezone = pytz.timezone("Asia/Tashkent")
    end_datetime = uzbekistan_timezone.localize(datetime.combine(assign_model.assign_link_foreign.end_date, assign_model.assign_link_foreign.end_time))
    start_datetime = uzbekistan_timezone.localize(datetime.combine(assign_model.assign_link_foreign.start_date, assign_model.assign_link_foreign.start_time))

    if request.method == "POST":
        current_datetime = timezone.now().astimezone(uzbekistan_timezone)
        if request.POST.get('BlockMe', None) == 'Block' and not (start_datetime < current_datetime < end_datetime):
            return render(
                request, 'testingsystem/Main_Page.html'
            )
        else:
            context = {"question_data": []}
            data = dict(request.POST)
            for key in data:
                if key.startswith("question_"):
                    val = data[key]
                    if key.endswith("_multi") and val[0]:
                        model = UserResponseModelMultiOption(
                            user=user,
                            question_based=questions[int(key.split("_")[1])],
                            answer_based=Option.objects.get(pk=int(val[0])),
                        )
                        model.save()
                    elif key.endswith("_truefalse"):
                        model = UserResponseModelTrueFalseOption(
                            user=user,
                            question_based=questions[int(key.split("_")[1])],
                            answer_based=True if val[0] == "true" else False,
                        )
                        model.save()
                    elif key.endswith("_freetext"):
                        model = UserResponseModelFreeTextOption(
                            user=user,
                            question_based=questions[int(key.split("_")[1])],
                            answer_based=val[0],
                        )
                        model.save()
            return redirect(
                reverse(
                    "UserScore:score",
                    kwargs={"user_id": user_id, "assign_slug": assign_slug},
                )
            )

    else:
        end_time = assign_model.limit_time.limited_datetime
        
        time = timezone.localtime(end_time, uzbekistan_timezone)

        question_data = [
            {
                "question_type": "multi"
                if question.options.all()
                else "truefalse"
                if question.truefalse.all()
                else "freetext",
                "text": mark_safe(question.text),
                "options": [
                    {"id": str(option.id), "text": mark_safe(option.answer)}
                    for option in Option.objects.filter(question=question)
                ]
                if question.options.all()
                else [],
            }
            for question in questions
        ]

        context = {
            "question_data": question_data,
            "user_id": user_id,
            "assign_slug": assign_slug,
            'end_time': time.isoformat(),
            'start_datetime': start_datetime.isoformat(),  
            'end_datetime': end_datetime.isoformat(),
        }
    return render(request, "userresponse/user_response1.html", context)


def registration_view(request, assign_id, assign_slug):
    assign_model = get_object_or_404(
        AssignLinkModel, pk=assign_id, slug_field=assign_slug
    )
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(
                reverse(
                    "UserResponse:responses",
                    kwargs={
                        "assign_id": assign_id,
                        "user_id": user.id,
                        "assign_slug": assign_slug,
                    },
                )
            )  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, "userresponse/register.html", {"form": form})


def previews_questions(request, test_id, preview_hash):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test)
    question_data = [
        {
            "question_type": "multi"
            if question.options.all()
            else "truefalse"
            if question.truefalse.all()
            else "freetext",
            "text": question.text,
            "options": [
                {"id": str(option.id), "text": option.answer}
                for option in Option.objects.filter(question=question)
            ]
            if question.options.all()
            else [],
        }
        for question in questions
    ]

    context = {"question_data": question_data}
    return render(request, "userresponse/user_response1.html", context)
    # else:
    #     return render(request, 'userresponse/user_response1.html', {"info":'Please this is illegal'})


def startTest(request, assign_id, assign_slug):
    assign_model = get_object_or_404(
        AssignLinkModel, pk=assign_id, slug_field=assign_slug
    )
    if request.method == "POST":
        print(request.POST)
        get_id = request.POST.get("start", None)
        if get_id:
            return redirect(
                reverse(
                    "UserResponse:register",
                    kwargs={"assign_id": int(get_id), "assign_slug": assign_slug},
                )
            )
    context = {"assign_id": assign_model.id}
    return render(request, "userresponse/startTest.html", context)

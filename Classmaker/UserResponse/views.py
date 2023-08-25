from django.shortcuts import render, redirect
from django.urls import reverse
from .models import UserResponseModelMultiOption, UserResponseModelFreeTextOption, UserResponseModelTrueFalseOption, \
    UserINFO
from TestingSystem.models import Question, Test, Option, TrueFalse, FreeText
from .forms import RegistrationForm
from django.utils.safestring import mark_safe


def answer_question_view(request, test_id, user_id, user_name):
    questions = Question.objects.all()
    user = UserINFO.objects.get(pk=user_id, surname=user_name)
    if request.method == 'POST':
        context = {'question_data': []}
        data = dict(request.POST)
        for key in data:
            if key.startswith('question_'):
                val = data[key]
                if key.endswith("_multi"):
                    model = UserResponseModelMultiOption(user=user, question_based=questions[int(key.split('_')[1])],
                                                         answer_based=Option.objects.get(pk=int(val[0])))
                    model.save()
                elif key.endswith('_truefalse'):
                    model = UserResponseModelTrueFalseOption(user=user,
                                                             question_based=questions[int(key.split('_')[1])],
                                                             answer_based=True if val[0] == 'true' else False)
                    model.save()
                elif key.endswith('_freetext'):
                    model = UserResponseModelFreeTextOption(user=user, question_based=questions[int(key.split('_')[1])],
                                                            answer_based=val[0])
                    model.save()
        return redirect(reverse('UserScore:score', kwargs={'user_id': user_id, 'user_name': user_name}))

    else:
        question_data = []
        for question in questions:
            question_obj = {
                "question_type": 'multi' if question.options.all() else 'truefalse' if question.truefalse.all() else 'freetext',
                "text": mark_safe(question.text),
            }
            if question_obj['question_type'] == 'multi':
                options = Option.objects.filter(question=question)
                question_obj["options"] = [{"id": option.id, "text": mark_safe(option.answer)} for option in options]
            question_data.append(question_obj)
        context = {'question_data': question_data}


    return render(request, 'userresponse/user_response1.html', context)


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(
                reverse('responses', kwargs={'test_id': 1, 'user_id': user.id,
                                             'user_name': user.slug}))  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'userresponse/register.html', {'form': form})

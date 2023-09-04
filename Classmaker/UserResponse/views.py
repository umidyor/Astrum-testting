from django.shortcuts import render, redirect, get_object_or_404
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
                if key.endswith("_multi") and val[0]:
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
        return redirect(reverse('UserScore:score', kwargs={'user_id': user_id, 'user_hashname': user_hashname}))


    else:
        question_data = [
            {
                "question_type": 'multi' if question.options.all() else 'truefalse' if question.truefalse.all() else 'freetext',
                "text": mark_safe(question.text),
                "options": [{"id": str(option.id), "text": mark_safe(option.answer)} for option in
                            Option.objects.filter(question=question)] if question.options.all() else []
            }
            for question in questions
        ]

        context = {'question_data': question_data, 'user_id':user_id, 'user_name':user_hashname}
    return render(request, 'userresponse/user_response1.html', context)


def registration_view(request, test_id):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('UserResponse:responses', kwargs={'test_id': test_id, 'user_id': user.id}))  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'userresponse/register.html', {'form': form})


def previews_questions(request, test_id, preview_hash):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test)
    question_data = [
        {
            "question_type": 'multi' if question.options.all() else 'truefalse' if question.truefalse.all() else 'freetext',
            "text": question.text,
            "options": [{"id": str(option.id), "text": option.answer} for option in
                        Option.objects.filter(question=question)] if question.options.all() else []
        }
        for question in questions
    ]

    context = {'question_data': question_data}
    return render(request, 'userresponse/user_response1.html', context)
    # else:
    #     return render(request, 'userresponse/user_response1.html', {"info":'Please this is illegal'})


def startTest(request, test_id):

    if request.method == 'POST':
        get_id = request.POST.get('start', None)
        if get_id:
            return redirect(reverse('UserResponse:register', kwargs={'test_id':int(get_id)}))
    context = {'test_id':test_id}
    return render(request, 'userresponse/startTest.html', context)
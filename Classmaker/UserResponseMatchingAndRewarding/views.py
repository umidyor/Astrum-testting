from django.shortcuts import render

# Create your views here.
from .models import UserResponseScore
from UserResponse.models import UserResponseModelMultiOption, UserResponseModelTrueFalseOption, \
    UserResponseModelMultiOption, UserINFO


def score(request, user_id, user_name):
    user = UserINFO.objects.get(pk=user_id, surname=user_name)
    score = 0
    mo_questions = user.user_multiple.all()
    tf_questions = user.user_truefalse.all()
    fr_questions = user.user_freetext.all()

    for mo in mo_questions:
        if mo.answer_based.is_correct:
            score += mo.question_based.ranking

    for tf in tf_questions:

        if tf.answer_based:
            if tf.question_based.truefalse.first().true:
                score += tf.question_based.ranking
        else:
            if tf.question_based.truefalse.first().false:
                score += tf.question_based.ranking

    for fr in fr_questions:
        if fr.answer_based == fr.question_based.freetext.first().freetext:
            score += fr.question_based.ranking
    model = UserResponseScore(user=user, score=score)
    model.save()
    context = {
        'score': score
    }
    return render(request, 'userscore/score.html', context)

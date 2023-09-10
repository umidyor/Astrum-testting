from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import UserResponseScore
from UserResponse.models import UserResponseModelMultiOption, UserResponseModelTrueFalseOption, \
    UserResponseModelMultiOption, UserINFO
from AssignLinks.models import AssignLinkModel


def score(request, user_id, assign_slug):
    assign_model = get_object_or_404(AssignLinkModel, slug_field=assign_slug)
    user = get_object_or_404(UserINFO, pk=user_id)
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

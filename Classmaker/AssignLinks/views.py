from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from TestingSystem.models import Test, TestQuestionRandomize
from .models import (
    AssignLinkModel,
    Availability,
    LimitTime,
    DisplayEachQuestion,
    NUMBER_CHOICES,
    TestCompletionModel,
    SendOffOn,
    CreatorEmailSendModel,
    TakerEmailSendModel,
)
from .forms import (
    AvailabilityForm,
    LimitTimeForm,
    DisplayEachQuestionForm,
    TestCompletionModelForm,
    SendOffOnForm,
    CreatorEmailSendModelForm,
    TakerEmailSendModelForm,
)
from django.utils import timezone
import pytz
from datetime import datetime, timedelta


def AssignLinkView(request, test_id, test_description):
    test = get_object_or_404(Test, pk=test_id, slug=test_description)
    if request.method == "GET":
        if request.GET.get("assign", None) == "True":
            return redirect(
                reverse(
                    "Assign:showed-assign",
                    kwargs={"test_id": test_id, "test_description": test_description},
                )
            )
    return render(request, "assignlinks/Assign.html")


def ShowLinks(request, test_id, test_description):
    test = get_object_or_404(Test, pk=test_id, slug=test_description)
    if request.method == "POST":
        form = AvailabilityForm(request.POST)
        time_limit_form = LimitTimeForm(request.POST)
        display_form = DisplayEachQuestionForm(request.POST)
        test_completion = TestCompletionModelForm(request.POST)
        sendoffon = SendOffOnForm(request.POST)
        creator_send = CreatorEmailSendModelForm(request.POST)
        taker_send = TakerEmailSendModelForm(request.POST)
        valid_values = all(
            [
                form.is_valid(),
                time_limit_form.is_valid(),
                display_form.is_valid(),
                test_completion.is_valid(),
                sendoffon.is_valid(),
                creator_send.is_valid(),
                taker_send.is_valid(),
            ]
        )
        if valid_values:
            formModel = form.save()
            formModeltime = time_limit_form.save()
            formModeldisplay = display_form.save()
            formModeltest = test_completion.save()
            formModeltaker = taker_send.save()
            if sendoffon.cleaned_data["off_or_no"]:
                formmodeloffon = sendoffon.save()
                sendoffon_id = formmodeloffon.id
                formmodel_creator = creator_send.save(commit=False)
                formmodel_creator.offno = SendOffOn.objects.get(pk=sendoffon_id)
                formmodel_creator.save()
            else:
                formmodel_creator = None
            av = Availability.objects.get(pk=formModel.id)
            lt = LimitTime.objects.get(pk=formModeltime.id)
            deq = DisplayEachQuestion.objects.get(pk=formModeldisplay.id)
            tcm = TestCompletionModel.objects.get(pk=formModeltest.id)
            tesm = TakerEmailSendModel.objects.get(pk=formModeltaker.id)
            cesm = (
                CreatorEmailSendModel.objects.get(pk=formmodel_creator.id)
                if formmodel_creator
                else None
            )
            model = AssignLinkModel(
                test_foreign=test,
                assign_link_foreign=av,
                limit_time=lt,
                display_each_question=deq,
                test_completion=tcm,
                creator_email_send=cesm,
                taker_email_send=tesm,
            )
            model.save(test.title)
            return redirect(reverse("Assign:copy-link", kwargs={"assign_id": model.id}))

    else:
        form = AvailabilityForm()
        time_limit_form = LimitTimeForm()
        display_form = DisplayEachQuestionForm()
        test_completion = TestCompletionModelForm()
        sendoffon = SendOffOnForm()
        creator_send = CreatorEmailSendModelForm()
        taker_send = TakerEmailSendModelForm()
    return render(
        request,
        "assignlinks/LinksShow.html",
        context={
            "form": form,
            "time_limit_form": time_limit_form,
            "display_form": display_form,
            "test_completion": test_completion,
            "sendoffon": sendoffon,
            "creator_send": creator_send,
            "taker_send": taker_send,
        },
    )


def ShowLinksEdit(request, assign_id, test_description):
    test = get_object_or_404(Test, slug=test_description)
    assign_link = get_object_or_404(AssignLinkModel, pk=assign_id)

    if request.method == "POST":
        form = AvailabilityForm(request.POST, instance=assign_link.assign_link_foreign)
        time_limit_form = LimitTimeForm(request.POST, instance=assign_link.limit_time)
        display_form = DisplayEachQuestionForm(
            request.POST, instance=assign_link.display_each_question
        )
        test_completion = TestCompletionModelForm(
            request.POST, instance=assign_link.test_completion
        )
        sendoffon = SendOffOnForm(
            request.POST, instance=assign_link.creator_email_send.offno
        )
        creator_send = CreatorEmailSendModelForm(
            request.POST, instance=assign_link.creator_email_send
        )
        taker_send = TakerEmailSendModelForm(
            request.POST, instance=assign_link.taker_email_send
        )

        valid_values = all(
            [
                form.is_valid(),
                time_limit_form.is_valid(),
                display_form.is_valid(),
                test_completion.is_valid(),
                sendoffon.is_valid(),
                creator_send.is_valid(),
                taker_send.is_valid(),
            ]
        )

        if valid_values:
            form.save()
            time_limit_form.save()
            display_form.save()
            test_completion.save()
            sendoffon.save()
            creator_send.save()
            taker_send.save()
            return redirect(
                reverse("Assign:copy-link", kwargs={"assign_id": assign_id})
            )

    else:
        form = AvailabilityForm(instance=assign_link.assign_link_foreign)
        time_limit_form = LimitTimeForm(instance=assign_link.limit_time)
        display_form = DisplayEachQuestionForm(
            instance=assign_link.display_each_question
        )
        test_completion = TestCompletionModelForm(instance=assign_link.test_completion)
        sendoffon = SendOffOnForm(instance=assign_link.creator_email_send.offno)
        creator_send = CreatorEmailSendModelForm(
            instance=assign_link.creator_email_send
        )
        taker_send = TakerEmailSendModelForm(instance=assign_link.taker_email_send)
    return render(
        request,
        "assignlinks/LinksShow.html",
        context={
            "form": form,
            "time_limit_form": time_limit_form,
            "display_form": display_form,
            "test_completion": test_completion,
            "sendoffon": sendoffon,
            "creator_send": creator_send,
            "taker_send": taker_send,
        },
    )


def CopyLinks(request, assign_id):
    model = get_object_or_404(AssignLinkModel, pk=assign_id)
    is_randomize = model.display_each_question.randomize
    if is_randomize:
        test_instance = model.test_foreign
        TestQuestionRandomize.randomize_questions(test_instance)

    context = {
        "assign_link": f"http://127.0.0.1:8000/users/start/online-test/{model.id}/{model.slug_field}/",
    }
    return render(request, "assignlinks/LinksCopy.html", context)


# def test_detail(request, assign_id):
#     test = Test.objects.get(slug=test_slug)

#     current_datetime = timezone.now().astimezone(timezone.pytz.timezone('Asia/Tashkent'))

#     start_datetime = timezone.pytz.timezone('Asia/Tashkent').localize(datetime.combine(test.availability.start_date, test.availability.start_time))
#     end_datetime = timezone.pytz.timezone('Asia/Tashkent').localize(datetime.combine(test.availability.end_date, test.availability.end_time))

#     if start_datetime <= current_datetime <= end_datetime:
#         return render(request, 'test_detail.html', {'test': test})
#     else:
#         return render(request, 'test_not_available.html')

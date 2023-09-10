from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Question, Test, Option, TrueFalse, FreeText
from .forms import TestForm, OptionForm, QuestionForm, DeleteForm, OptionFormSet, TrueFalseFormSet, TrueFalseForm, \
    FreeTextFormSet, FreeTextForm

from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)




def home(request):
    if request.method == 'POST':
        form = TestForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                create_question = reverse(
                    'TestingSystem:tests')
                return redirect(create_question)
            except:
                form.add_error(None, "Some problems with filling blank")
    else:
        form = TestForm()

    data = {
        'form': form
    }
    return render(request, 'testingsystem/temp.html', data)


class CreateQuestionAndOptions:

    def __init__(self, request, test):
        self.request = request
        self.test = test

    def DatabaseSave(self, QForm, OptionalFormSet):
        question_form = QForm(self.request.POST)
        formset = OptionalFormSet(self.request.POST)
        if question_form.is_valid() and formset.is_valid():
            question = question_form.save(commit=False)
            question.test = self.test
            question.save(self.test.description)
            formset_instances = formset.save(commit=False)

            for form in formset_instances:
                form.question = question
                form.save()
            return [question_form, formset, True]


def CreateQuestionAndMultpleOptions(request, test_id, test_description):
    test = Test.objects.get(pk=test_id, slug=test_description)
    if request.method == 'POST':
        print(request.POST, request.FILES)

        CQAP = CreateQuestionAndOptions(request, test)
        question_form, option_formset, is_valid = CQAP.DatabaseSave(QuestionForm, OptionFormSet)
        if is_valid:
            object_list = reverse('TestingSystem:tests')
            return redirect(object_list)
    else:
        question_form = QuestionForm()
        option_formset = OptionFormSet(queryset=Option.objects.none())

    return render(request, 'testingsystem/main.html', {
        'question_form': question_form,
        'option_formset': option_formset,
        'slug': test.slug,
        'test_id': test_id,
        'id': request.GET.get('id', None),
    })


def CreateQuestionAndTrueFalseOptions(request, test_id, test_description):
    test = Test.objects.get(pk=test_id, slug=test_description)
    if request.method == 'POST':
        CQAP = CreateQuestionAndOptions(request, test)
        question_form, truefalse_formset, is_valid = CQAP.DatabaseSave(QuestionForm, TrueFalseFormSet)
        if is_valid:
            object_list = reverse('TestingSystem:tests')
            return redirect(object_list)  # Replace with the actual success URL

    else:
        question_form = QuestionForm()
        truefalse_formset = TrueFalseFormSet(queryset=TrueFalse.objects.none())

    return render(request, 'testingsystem/main.html', {
        'question_form': question_form,
        'option_formset': truefalse_formset,
        'slug': test.slug,
        'test_id': test_id,
    })


def CreateQuestionAndFreeTextOptions(request, test_id, test_description):
    test = Test.objects.get(pk=test_id, slug=test_description)
    if request.method == 'POST':
        CQAP = CreateQuestionAndOptions(request, test)
        question_form, freetext_formset, is_valid = CQAP.DatabaseSave(QuestionForm, FreeTextFormSet)
        if is_valid:
            object_list = reverse('TestingSystem:tests')
            return redirect(object_list)  # Replace with the actual success URL
    else:
        question_form = QuestionForm()
        freetext_formset = FreeTextFormSet(queryset=FreeText.objects.none())

    return render(request, 'testingsystem/main.html', {
        'question_form': question_form,
        'option_formset': freetext_formset,
        'slug': test.slug,
        'test_id': test_id,
    })


class EditQuestionAndOptions:

    def __init__(self, request, question, options):
        self.request = request
        self.question = question
        self.options = options

    def DatabaseEdit(self, QForm, OptionalForm):
        form = QForm(self.request.POST, instance=self.question)
        option_forms = [OptionalForm(self.request.POST, instance=option, prefix=f'option_{option.id}') for option in
                        self.options]
        if form.is_valid() and all(of.is_valid() for of in option_forms):
            form.save()
            for option_form in option_forms:
                option_form.save()
            return [form, option_forms, True]


def EditQuestionAndMultpleOptions(request, question_id, question_description):
    question = get_object_or_404(Question, pk=question_id, slug=question_description)
    options = Option.objects.filter(question=question)
    if request.method == 'POST':
        EQAO = EditQuestionAndOptions(request, question, options)
        form, option_forms, is_valid = EQAO.DatabaseEdit(QuestionForm, OptionForm)
        if is_valid:
            reverse_url = reverse('TestingSystem:tests')
            return redirect(reverse_url)
    else:
        form = QuestionForm(instance=question)
        option_forms = [OptionForm(instance=option, prefix=f'option_{option.id}') for option in options]
    return render(request, 'testingsystem/question_edit.html', {'form': form, 'option_forms': option_forms})


def EditQuestionAndTrueFalseOptions(request, question_id, question_description):
    print(question_id)
    question = get_object_or_404(Question, pk=question_id, slug=question_description)
    options = TrueFalse.objects.filter(question=question)
    if request.method == 'POST':
        EQAO = EditQuestionAndOptions(request, question, options)
        form, truefalse_forms, is_valid = EQAO.DatabaseEdit(QuestionForm, TrueFalseForm)
        if is_valid:
            reverse_url = reverse('TestingSystem:tests')
            return redirect(reverse_url)
    else:
        form = QuestionForm(instance=question)
        truefalse_forms = [TrueFalseForm(instance=option, prefix=f'option_{option.id}') for option in options]
    return render(request, 'testingsystem/question_edit.html', {'form': form, 'option_forms': truefalse_forms})


def EditQuestionAndFreeTextOptions(request, question_id, question_description):
    question = get_object_or_404(Question, pk=question_id, slug=question_description)
    options = FreeText.objects.filter(question=question)
    if request.method == 'POST':
        EQAO = EditQuestionAndOptions(request, question, options)
        form, freetext_forms, is_valid = EQAO.DatabaseEdit(QuestionForm, FreeTextForm)
        if is_valid:
            reverse_url = reverse('TestingSystem:tests')
            return redirect(reverse_url)
    else:
        form = QuestionForm(instance=question)
        freetext_forms = [FreeTextForm(instance=option, prefix=f'option_{option.id}') for option in options]
    return render(request, 'testingsystem/question_edit.html', {'form': form, 'option_forms': freetext_forms})


def TestViews(request):
    test = Test.objects.all()
    if request.method == "GET":
        if request.GET.get('alpabetical', None)=='True':
            sorted_test = test.order_by('title')
        elif request.GET.get('resent', None) == 'True':
            sorted_test = test.order_by('-testCreatedTime')
        else:
            sorted_test = test
    else:
        sorted_test = test
    return render(request, 'testingsystem/Test.html', {'objects': sorted_test})


def main_page(request):
    return render(request, 'testingsystem/Main_Page.html')


def QuestionView(request, test_id, test_description):
    test = get_object_or_404(Test, pk=test_id, slug=test_description)
    questions = Question.objects.filter(test=test)
    if request.method == "POST":
        deleteTestId = request.POST.get('test_id', None)
        deletequestionId = request.POST.get('question_delete_id', None)
        if deleteTestId is not None:
            if test.id == int(deleteTestId):
                test.delete()
                reverse_url = reverse('TestingSystem:tests')
                return redirect(reverse_url)

        if deletequestionId is not None:
            dquestion = Question.objects.filter(pk=int(deletequestionId))
            dquestion.delete()

    q_and_a = [
        {
            'Q_ID': question.id,
            'Q_N': idx + 1,
            'question_description': question.slug,
            'text': question.text,
            'ranking': question.ranking,
            'qtype': 'multiple' if question.options.all() else 'freetext' if question.freetext.all() else 'truelfalse',
            'answers': [answers for answers in
                        list(question.options.all()) + list(question.freetext.all()) + list(question.truefalse.all())]
        }
        for idx, question in enumerate(questions)]

    encrypted_data = cipher_suite.encrypt(test.slug.encode())

    context = {
        'slug': test.slug,
        'test_id': test.id,
        'questions': q_and_a,
        'preview_hash': encrypted_data.decode()[:-2],
    }
    return render(request, 'testingsystem/questions.html', context=context)

# from django.shortcuts import render
# from django.http import JsonResponse

# def initial_content_view(request):
#     return render(request, 'testingsystem/initial_content.html')
#
# def new_content_view(request):
#     return render(request, 'testingsystem/new_content.html')

# Generate a random encryption key

# Create a Fernet cipher object with the key

# Input data to be encrypted

# Encrypt the data

# Decrypt the data to retrieve the original input

# Display the results

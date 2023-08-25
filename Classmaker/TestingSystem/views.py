from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Question, Test, Option, TrueFalse, FreeText
from .forms import TestForm, OptionForm, QuestionForm, DeleteForm, OptionFormSet, TrueFalseFormSet, TrueFalseForm, \
    FreeTextFormSet, FreeTextForm


def home(request):
    if request.method == 'POST':
        form = TestForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                create_question = reverse(
                    'TestingSystem:tests')  # kwargs={"test_id": test.id, "test_description": test.slug})
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
            question.save(self.test.title)
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
        'id': request.GET.get('id'),
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


def EditQuestionAndMultpleOptions(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    options = Option.objects.filter(question=question)
    if request.method == 'POST':
        EQAO = EditQuestionAndOptions(request, question, options)
        form, option_forms, is_valid = EQAO.DatabaseEdit(QuestionForm, OptionForm)
        if is_valid:
            reverse_url = reverse('TestingSystem:tests')
            return redirect(reverse_url)  # Redirect to a list view of questions
    else:
        form = QuestionForm(instance=question)
        option_forms = [OptionForm(instance=option, prefix=f'option_{option.id}') for option in options]
    return render(request, 'testingsystem/question_edit.html', {'form': form, 'option_forms': option_forms})


def EditQuestionAndTrueFalseOptions(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    options = TrueFalse.objects.filter(question=question)
    if request.method == 'POST':
        EQAO = EditQuestionAndOptions(request, question, options)
        form, truefalse_forms, is_valid = EQAO.DatabaseEdit(QuestionForm, TrueFalseForm)
        if is_valid:
            reverse_url = reverse('TestingSystem:tests')
            return redirect(reverse_url)  # Redirect to a list view of questions
    else:
        form = QuestionForm(instance=question)
        truefalse_forms = [TrueFalseForm(instance=option, prefix=f'option_{option.id}') for option in options]
    return render(request, 'testingsystem/question_edit.html', {'form': form, 'option_forms': truefalse_forms})


def EditQuestionAndFreeTextOptions(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    options = FreeText.objects.filter(question=question)
    if request.method == 'POST':
        EQAO = EditQuestionAndOptions(request, question, options)
        form, freetext_forms, is_valid = EQAO.DatabaseEdit(QuestionForm, FreeTextForm)
        if is_valid:
            reverse_url = reverse('TestingSystem:tests')
            return redirect(reverse_url)  # Redirect to a list view of questions
    else:
        form = QuestionForm(instance=question)
        freetext_forms = [FreeTextForm(instance=option, prefix=f'option_{option.id}') for option in options]
    return render(request, 'testingsystem/question_edit.html', {'form': form, 'option_forms': freetext_forms})


class DeleteQuestionView(DeleteView):
    model = Question
    template_name = 'testingsystem/delete_question.html'
    success_url = reverse_lazy('TestingSystem:tests')
    from_class = DeleteForm


class DeleteTestView(DeleteView):
    model = Test
    template_name = 'testingsystem/delete_test.html'
    success_url = reverse_lazy('TestingSystem:tests')
    from_class = DeleteForm


def TestViews(request):
    return render(request, 'testingsystem/index.html', {'objects': Test.objects.all()})
